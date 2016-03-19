#!/usr/bin/env python3
import requests
import ujson
import sys
import argparse
import ipaddress

apiurl = 'https://www.peeringdb.com/api/'

parser = argparse.ArgumentParser(description='A small tool for querying PeeringDB.net')
parser.add_argument('search', metavar='<search_term>', help='Search string. ASN, IP or Company Name')
parser.add_argument('--fac', action='store_true', help='Search by Colocation Facilities')
parser.add_argument('--ix', action='store_true', help='Search by Internet Exchange')
parser.add_argument('-v', action='store_true', help='Verbose output')
args = parser.parse_args()


def fetchResults(url):
    response = requests.get(url)
    response = ujson.loads(response.text)
    return response

# Matches an ASN and provides info
def whois(search):
    url = "%snet?asn=%s&depth=2" % (apiurl, search)
    results = fetchResults(url)
    if not results['data']:
        print("AS%s not found in PeeringDB" % search)
        exit(1)
    print("name: %s" % results['data'][0].pop('name'))
    if results['data'][0]['aka'] is not "":
        print("aka: %s" % results['data'][0].pop('aka'))
    if args.v:
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

# Searches for an IX and provides info
def findIX(search):
    # First try to match exact name
    url = "%six?name=%s" % (apiurl, search)
    results = fetchResults(url)
    # If we find nothing, do a loose match on the search
    if not results['data']:
        url = "%six?name__contains=%s" % (apiurl, search)
        results = fetchResults(url)
        if not results['data']:
            print("No matches for %s" % (search))
            return  # Nothing found return to main()

    for ix in results['data']:
        ix_id = ix['id']
        print("Internet Exchange: %s" % ix['name'])
        try:
            print("\tcity: %s" % ix['city'])
            print("\tcountry: %s" % ix['country'])
            print("\twebsite: %s" % ix['website'])
            print("\ttech_phone: %s" % ix['tech_phone'])
        except:
            pass

        # If verbose, find out what networks are present on the IXLAN
        if args.v:
            print("Networks Present:")
            url2 = "%snetixlan?ix_id=%s" % (apiurl, ix_id)
            results2 = fetchResults(url2)
            for net in results2['data']:
                print("\t%s - AS%s" % (lookupNet(net['net_id']), net['asn']))


def findFac(search):
    url = "%sfac?name__contains=%s" % (apiurl, search)
    results = fetchResults(url)
    if not results['data']:
        print("No matches for %s" % (search))
    else:
        for fac in results['data']:
            fac_id = fac['id']
            print("Facility Name: %s" % fac['name'])
            if args.v:
                print("Networks:")
                url2 = "%snetfac?fac_id=%s" % (apiurl, fac_id)
                results2 = fetchResults(url2)
                for net in results2['data']:
                    print("\t%s - AS%s" % (lookupNet(net['net_id']), net['local_asn']))

# Searches the results for Company name and spits out the ASN
def findASN(search):
    url = "%snet?name__contains=%s" % (apiurl, search)
    results = fetchResults(url)
    if not results['data']:
        print("No matches for %s" % (search))
    else:
        for result in results['data']:
            print("%s: AS%s in %s" % (result['name'], result['asn'], result['info_scope']))

def lookupNet(search):
    url = "%snet?id=%s" % (apiurl, search)
    results = fetchResults(url)
    return results['data'][0]['name']

def lookupIXLAN(search):
    url = "%sixlan?id=%s" % (apiurl, search)
    results = fetchResults(url)
    url = "%six?id=%s" % (apiurl, results['data'][0]['ix_id'])
    results = fetchResults(url)
    return results['data'][0]['name']

# Searches pdb for who is peering and at which IX, with a given IP address
def findIP(ip):
    if ip.version == 4:
        url = "%snetixlan?ipaddr4=%s" % (apiurl, ip)
    elif ip.version == 6:
        url = "%snetixlan?ipaddr6=%s" % (apiurl, ip)

    results = fetchResults(url)
    if not results['data']:
        print("No matches for %s" % (ip))
    else:
        for result in results['data']:
            netName = lookupNet(result['net_id'])
            ixlanName = lookupIXLAN(result['ixlan_id'])
            if result['is_rs_peer'] == "true":
                RS = "with the route servers "
            else:
                RS = ""
            print("%s - AS%s is peering %sat %s on %s" % (netName, result['asn'], RS, ixlanName, ip))
            if args.v:
                for key in sorted(result):
                    print("%s: %s" % (key, result[key]))


def main():

    search = args.search

    # Strip leading "AS" and check to see if what remains is an integer
    # So we don't accidentally catch company names starting with "AS"
    if (search[0:2] == "AS" or search[0:2] == "as") and search[2:].isdigit():
        search = search[2:]

    # See if search string is an IP address
    ip = None
    try:
        ip = ipaddress.ip_address(search)
    except:
        pass

    if ip is not None:
        findIP(ip)
    elif args.ix:
        findIX(search)
    elif args.fac:
        findFac(search)
    elif search.isdigit():
        whois(search)
    else:
        findASN(search)


if __name__ == "__main__":
    main()
