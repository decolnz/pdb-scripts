#!/usr/bin/env python3
import requests
import ujson
import sys

apiurl = 'https://www.peeringdb.com/api/net'
#options = ('depth=2')
options = None


def fetchResults(url):
    response = requests.get(url)
    response = ujson.loads(response.text)
    return response

def main():

    if len(sys.argv) != 2 or sys.argv[1] == "--help":
        print("pdbfindasn.py - A quick tool to search PeeringDB.net for a company name and return its ASN")
        print("Usage: ./pdbfindasn.py <Company Name>")
        exit(1)
    else:
        search = sys.argv[1]

    if options is not None:
        if isinstance(options, str):
            opts = options
        else:
            opts = str("&").join(options)
        url = "%s?name__contains=%s&%s" % (apiurl, search, opts)
    else:
        url = "%s?name__contains=%s" % (apiurl, search)

    results = fetchResults(url)
    if not results['data']:
        print("No matches for %s" % (search))
    else:
        for result in results['data']:
            print("%s: AS%s in %s" % (result['name'], result['asn'], result['info_scope']))

if __name__ == "__main__":
    main()
