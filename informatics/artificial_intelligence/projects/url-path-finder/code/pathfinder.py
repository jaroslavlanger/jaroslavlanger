#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL Path Finder - find a path from one site to another just by clicking links.

2021 Feb 08, Jaroslav Langer
"""

import sys
import requests
import re

def get_tlds():
    # Download domains form iana.org
    resp_tlds = requests.request(method='get', url='https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    # Remove first line (date), last line (empty)
    tlds = resp_tlds.text.split('\n')[1:-1]
    return tlds


def get_url_regex_obj():
    tlds = get_tlds()

    scheme = r'(https?)?:?\/*(www\.)?'

    vbs = r'(\s|\A|\(|\{|\[|\'|\")' # Valid Beginning Separator
    user = r'[-a-zA-Z0-9._+~]{1,256}@'
    host = r'[-a-zA-Z0-9._+~]{1,256}'
    port = r':[0-9]{0,5}'
    domains = '|'.join(tlds)
    path = r'/[-a-zA-Z0-9()@:%_+.~&=/]*'
    query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'
    ves = r'(\s|\Z|\)|\}|\]|\'|\")' # Valid Ending Separator

    pattern_url = fr'{vbs}{scheme}(({user})?{host}({port})?\.({domains})({path})?){query_fragment}{ves}'

    return re.compile(pattern_url, flags=re.IGNORECASE)


def standardize_url(url):
    return f'https://{url[:-1]}' if (url.endswith('/')) else f'https://{url}'


class UrlPathFinder():
    """Class for URL traveler"""

    url_regex_obj = None
    links = None
    links_dict = None
    visited = None
    end = None
    ignore_url_inside = '@'
    ignored_url_ends = [    # Sites ending with following ends are ignored
            '.jpg', '.jpeg', '.png', '.ico', '.gif', '.svg',    # Images
            '.mp3',                                             # Music
            '.mov', '.mp4',                                     # Video
            '.css', '.json', '.js',                             # Code
            '()', '(',                                          # Discutable
    ]
    route = None

    @classmethod
    def get_links_from_url(cls, url):
        links = set()
        try:
            response = requests.request(
                    method='get', url=url,
                    # verify=False,
            )
            cls.visited[url] = cls.links_dict[url]
            if (cls.file_log is not None):
                print( f'VISITED:    {url} <- {cls.visited[url]}',
                        file=cls.file_log)
            # cls.visited.add(url);

            findings = cls.url_regex_obj.findall(response.text)

            links = {standardize_url(tup[3]) for tup in findings}

        except requests.exceptions.SSLError as e:
            print('ERROR:      requests.exceptions.SSLError occured',
                    f'ignored: {e}', sep=', ', file=sys.stderr)
        except requests.exceptions.ConnectionError as e:
            print('ERROR:      requests.exceptions.ConnectionError occured',
                    f'ignored: {e}', sep=', ', file=sys.stderr)
        except requests.exceptions.InvalidURL as e:
            print('ERROR:      requests.exceptions.InvalidURL occured',
                    f'ignored: {e}', sep=', ', file=sys.stderr)
        except UnicodeError as e:
            print('ERROR:      UnicodeError occured',
                    f'ignored: {e}', sep=', ', file=sys.stderr)

        return links


    @classmethod
    def is_route_complete(cls, links):
        """
        Return True or False depending whether the end url is in the links.
        If True, cls.route is set with list from start url to end url.
        """
        last_links = [link for link in links if (cls.end in link)]
        if (len(last_links) > 0):
            if (cls.file_log is not None):
                print('\n    EUREKA!\n', file=cls.file_log)

            last_link = last_links[0]   # Chose some of the final sites
            cls.route = [last_link]
            prev_url = links[last_link]
            while (prev_url is not None):
                cls.route.insert(0, prev_url)
                prev_url = cls.visited[prev_url]
            return True
        return False


    @classmethod
    def bfs(cls, level=0):
        next_links = {}

        for url in cls.links:
            links_set = cls.get_links_from_url(url)

            links_dict = {
                    link: url for link in links_set if (
                            (all((not link.endswith(s_type)
                                    for s_type in cls.ignored_url_ends)))
                            and ('@' not in link)
                            and (link not in cls.links)
                            and (link not in cls.visited)
                    )
            }

            if (cls.is_route_complete(links_dict)):
                return cls.route

            # Add links, with accepted type that are not duplicated
            next_links.update(links_dict)

        if (cls.file_log is not None):
            print(f'LEVEL:      {level}', file=cls.file_log)
            print(f'NEXT_LINKS: {next_links}', file=cls.file_log)

        cls.links_dict = next_links
        cls.links = [link for link in next_links if f'.{cls.end_domain}' in link]
        cls.links.extend([link for link in next_links if (link not in cls.links)])

        return cls.bfs(level+1)


    @classmethod
    def find_route(cls, site_start, site_end, method, file_out, file_log):
        """Find route between site_start and site_end by following links"""

        cls.file_log = file_log

        cls.url_regex_obj = get_url_regex_obj() # Pattern for url matching

        end_groups = cls.url_regex_obj.findall(site_end)[0] # Match site_end
        cls.end = end_groups[3]
        if cls.end.endswith('/'):               # Trim ending '/'
            cls.end = cls.end[:-1]
        cls.end_domain = end_groups[6]          # Set end domain (for priority)

        start_url = standardize_url(
                cls.url_regex_obj.findall(site_start)[0][3]
        )

        cls.links = [start_url]
        cls.links_dict = {start_url: None}
        cls.visited = {}

        if (method.lower() == 'bfs'):
            cls.bfs()
        else:
            raise NotImplementedError(
                    'This search method is not implemented yet, try bfs'
            )

        print(' -> '.join(cls.route), file=file_out)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
            '-s', '--start', type=str, default='www.fit.cvut.cz',
            help='site where the route starts, www.fit.cvut.cz by default',

    )
    parser.add_argument(
            '-e', '--end', type=str, default='www.mit.edu',
            help='site where the route should end, www.mit.edu by default',
    )
    parser.add_argument(
            '-d', '--debug', action='store_true', help='run in debug mode',
    )
    parser.add_argument(
            '-m', '--method', default='bfs', choices=['ids', 'dfs', 'bfs'],
            help='search algorithm choice',
    )
    parser.add_argument(
            '-l', '--logging', nargs='?', const=sys.stdout, default=None,
            type=argparse.FileType('w'),
            help=('optional metadata logging, default option is logging off, '
                    'if set without file, stdout is used')
    )
    parser.add_argument(
            '-o', '--output', type=argparse.FileType('w'),
            default=sys.stdout,
            help='output file, if not given, stdout is used'
    )
    args = parser.parse_args()


    if (args.debug):
        import pdb; pdb.set_trace()

    UrlPathFinder.find_route(
            site_start=args.start, site_end=args.end,
            method=args.method, file_out=args.output, file_log=args.logging
    )
