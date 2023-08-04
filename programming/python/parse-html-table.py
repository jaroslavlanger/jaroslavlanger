#!/usr/bin/env python3
"""Parses table after specified element from given HTML.

Example: `python3 parse-html-table.py products h2 < site.html`

For every level 2 heading containing the word "products",
the first following table will be written to the standard output.
"""
import sys
from html.parser import HTMLParser

class State: ...
class RequiredElem(State): ...
class Parsing(State): ...
class Header(Parsing): ...
class HeaderCell(Header): ...
class Body(Parsing): ...
class Row(Body): ...
class RowCell(Row): ...

def table_to_csv(header, rows):
    return "\n".join(['\t\t'.join(row) for row in [header, *rows]])

"""
HTML element description
    'html'      # top-level "root" element
    'h2',       # heading level 2
    'table'     # contains table rows or rows encapsulation elements (thead tbody)
    'thead',    # defines descendant rows as the table header
    'tbody',    # defines descendant rows as the table body
    'tr',       # table row
    'th',       # header cell (of table row)
    'td',       # data cell (of table row)
"""
class TableParser(HTMLParser):

    def __init__(self, req_text='', req_elem=None):
        """
        req_text: string which must occur in the required element (if specified).
        req_elem: html element whose body must contain the required string.
        """
        super().__init__()
        self.req_text = req_text
        self.req_elem = req_elem

        self.state = State

        self.header_cell = []
        self.header = []
        self.row = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        self.state = ({'thead': Header,
                       'th': HeaderCell,
                       'tbody': Body,
                       'tr': Row,
                       'td': RowCell,
                      }.get(tag, self.state)
            if issubclass(self.state, Parsing) else
                      (RequiredElem if tag == self.req_elem else self.state)
        )

    def handle_data(self, data):
        if issubclass(self.state, RequiredElem) and self.req_text in data.lower():
            self.state = Parsing
        elif issubclass(self.state, HeaderCell):
            self.header_cell.append(data)
        elif issubclass(self.state, RowCell):
            self.row.append(data)

    def handle_endtag(self, tag):
        if issubclass(self.state, RequiredElem) and tag == self.req_elem:
            self.state = State
        elif issubclass(self.state, HeaderCell) and tag == 'th':
            self.header.append(' '.join(part.strip() for part in self.header_cell)); self.header_cell = []
            self.state = Header
        elif issubclass(self.state, Header) and tag == 'thead':
            self.state = Parsing
        elif issubclass(self.state, RowCell) and tag == 'td':
            self.state = Row
        elif issubclass(self.state, Row) and tag == 'tr':
            self.rows.append(tuple(self.row)); self.row = []
            self.state = Body
        elif issubclass(self.state, Body) and tag == 'tbody':
            print(table_to_csv(self.header, self.rows))
            self.state = State

if __name__ == '__main__':
    TableParser(*sys.argv[1:]).feed(sys.stdin.read())
