#!/usr/bin/env python3
import requests
import ujson
import sys

apiurl = 'https://www.peeringdb.com/api/net'
ixurl = 'https://www.peeringdb.com/api/ix'
facurl = 'https://www.peeringdb.com/api/fac'
options = ('depth=2')


def fetchResults(url):
    response = requests.get(url)
    response = ujson.loads(response.text)
    return response

def main():

    if len(sys.argv) != 2:
        print("Usage: ./pdbwhois.py <ASN>")
        exit(1)

    if isinstance(options, str):
        opts = options
    else:
        opts = str("&").join(options)

    url = "%s?asn=%s&%s" % (apiurl, sys.argv[1], opts)
    #print(url)
    results = fetchResults(url)
    for key in sorted(results['data'][0]):
        if key == 'netixlan_set':
            print("Peering at:")
            for ixlan in results['data'][0][key]:
                url = "%s?ixlan_id=%s" % (ixurl, ixlan['ixlan_id'])
                ix_results = fetchResults(url)
                print("\t%s " % ix_results['data'][0]['name'])
        elif key == 'netfac_set':
            print("Present at:")
            for fac in results['data'][0][key]:
                url = "%s?id=%s" % (facurl, fac['fac_id'])
                fac_results = fetchResults(url)
                print("\t%s " % fac_results['data'][0]['name'])
        elif results['data'][0][key] is not "":
            print("%s: %s" % (key, results['data'][0][key]))

    #print(results['data'][0])

if __name__ == "__main__":
    main()
