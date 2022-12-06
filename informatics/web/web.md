# Web

`2021 Feb 18, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Domain Name System](#domain-name-system)
* [DNS records](#dns-records)
* [Domain Name](#domain-name)
* [Uniform Resource Locator (URL)](#uniform-resource-locator-url)
* [Hostname](#hostname)
* [Port](#port)

<!-- /TOC -->

## References

* [Getting started with the web - Dealing with files (mozilla.org)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files)

## Domain Name System

* [Domain Name System (wikipedia.org)](https://en.wikipedia.org/wiki/Domain_Name_System)

## DNS records

* [List of DNS record types (wikipedia.org)](https://en.wikipedia.org/wiki/List_of_DNS_record_types)

## Domain Name

* [Domain name (wikipedia.org)](https://en.wikipedia.org/wiki/Domain_name)

Any name registered in the Domain Name System (DNS) is a domain name.

All domains are subdomains of the DNS root domain which is nameless.
Top level domains TLDs such as com, org, ...

For example: the label `example` specifies a node `example.com` as a subdomain of the `com` domain, and `www` is a label to create `www.example.com`, a subdomain of `example.com`.

* [TLD List (wiki.mozilla.org)](https://wiki.mozilla.org/TLD_List)
* [List of TLDs in the root DNS](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

## Uniform Resource Locator (URL)

* [URL (wikipedia.org)](https://en.wikipedia.org/wiki/URL)

```
URI = scheme:[//authority]path[?query][#fragment]
```

```
authority = [userinfo@]host[:port]
```

## Hostname

Hostnames are composed of a sequence of labels concatenated with dots. For example, "en.wikipedia.org" is a hostname. Each label must be from 1-63 characters long. The entire hostname, including the dots, has a maximum of 253 characters.

The Internet standards (Requests for Comments)  specify that labels may contain only `[a-zA-Z0-9]`.

* [Hostname (wikipedia.org)](https://en.wikipedia.org/wiki/Hostname)

## Port

A port number is a 16-bit unsigned integer, thus ranging from 0 to 65535.

* [Port (computer networking)](https://en.wikipedia.org/wiki/Port_(computer_networking))
