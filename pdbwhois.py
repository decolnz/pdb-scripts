#!/usr/bin/env python3
import requests
import ujson
import sys

apiurl = 'https://www.peeringdb.com/api/'

def fetchResults(url):
    response = requests.get(url)
    response = ujson.loads(response.text)
    return response

def whois(search):
    # Matches an ASN and provides info_scope
    url = "%snet?asn=%s&depth=2" % (apiurl, search)
    results = fetchResults(url)
    for key in sorted(results['data'][0]):
        if key == 'netixlan_set':
            print("Peering at:")
            for ixlan in results['data'][0][key]:
                url = "%six?ixlan_id=%s" % (apiurl, ixlan['ixlan_id'])
                ix_results = fetchResults(url)
                print("\t%s " % ix_results['data'][0]['name'])
        elif key == 'netfac_set':
            print("Present at:")
            for fac in results['data'][0][key]:
                url = "%sfac?id=%s" % (apiurl, fac['fac_id'])
                fac_results = fetchResults(url)
                print("\t%s " % fac_results['data'][0]['name'])
        elif results['data'][0][key] is not "":
            print("%s: %s" % (key, results['data'][0][key]))


def findASN(search):
    # Searches the results for Company name and spits out the ASN
    url = "%snet?name__contains=%s" % (apiurl, search)
    results = fetchResults(url)
    if not results['data']:
        print("No matches for %s" % (search))
    else:
        for result in results['data']:
            print("%s: AS%s in %s" % (result['name'], result['asn'], result['info_scope']))

def main():

    if len(sys.argv) != 2:
        print("Usage: ./pdbwhois.py <ASN>")
        exit(1)
    else:
        search = sys.argv[1]

    # Strip leading "AS" and check to see if what remains is an integer
    # So we don't accidentally catch company names starting with "AS"
    if (search[0:2] == "AS" or search[0:2] == "as") and search[2:].isdigit():
        search = search[2:]

    if search.isdigit():
        whois(search)
    else:
        findASN(search)


if __name__ == "__main__":
    main()
