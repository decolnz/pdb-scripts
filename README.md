PeeringDB Scripts
=================

Random scripts resulting from playing around with the new [PeeringDB](https://peeringdb.net) APIs

Usage:
------

    usage: pdbwhois.py [-h] [-v] search

    A small tool for querying PeeringDB.net

    positional arguments:
      search      Search string. ASN or Company Name

    optional arguments:
      -h, --help  show this help message and exit
      -v          Verbose output

Examples:
--------

    $ ./pdbwhois.py bbc
    BBC: AS2818 in Global
    BBC R&D: AS31459 in Regional

    $ ./pdbwhois.py 2818
    name: BBC
    aka: BBC, BBC Internet Services, BBC Technology

    $ ./pdbwhois.py 2818 -v
    name: BBC
    aka: BBC, BBC Internet Services, BBC Technology
    asn: 2818
    created: 2004-07-28T00:00:00Z
    id: 17
    info_ipv6: False
    info_multicast: False
    info_prefixes4: 7
    info_prefixes6: 0
    info_ratio: Heavy Outbound
    info_scope: Global
    info_traffic: 20-50 Gbps
    info_type: Content
    info_unicast: True
    irr_as_set: AS-BBC
    Present at:
    	Telehouse London (Docklands North)
    	Telehouse London (Docklands East)
    	TelecityGroup London (Sovereign House)
    	TelecityGroup Amsterdam 2 (South East)
    	Telehouse London (Docklands West)
    Peering at:
    	LINX Extreme LAN
    	LINX Juniper LAN
    	LONAP
    	LONAP
    	AMS-IX
    	DE-CIX Frankfurt
    	IXManchester
    notes: AS2818 in the UK/EU
    AS9156 is the transit AS

    the BBC is not currently accepting requests for peering at this exchange point
    org_id: 50
    poc_set: []
    policy_contracts: Not Required
    policy_general: Open
    policy_locations: Not Required
    policy_ratio: False
    policy_url: http://support.bbc.co.uk/support/peering/
    status: ok
    updated: 2016-03-14T20:57:33Z
    website: http://www.bbc.co.uk
