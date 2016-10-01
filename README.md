PeeringDB Tool
=================

A small search tool resulting from playing around with the new [PeeringDB](https://peeringdb.com) [APIs](https://www.peeringdb.com/apidocs/)

Install:
---------------

Clone the git repository:

    git clone https://github.com/detobate/pdb-scripts.git

Install python3 and the required python modules if you don't already have them:

    sudo apt-get install python3 python3-pip
    sudo pip3 install -r ./pdb-scripts/requirements.txt

Optionally add an alias for the script to your ~/.bash_profile for easier execution

    echo "alias pdb='`pwd`/pdb-scripts/pdbwhois.py'" >> ~/.bash_profile

Usage:
------

    usage: pdbwhois.py [-h] [--fac] [--ix] [-v] <search_term>

    A small tool for querying PeeringDB.com

    positional arguments:
    <search_term>  Search string. ASN, IP or Company Name

    optional arguments:
    -h, --help     show this help message and exit
    --fac          Search by Colocation Facilities
    --ix           Search by Internet Exchange
    -v             Verbose output

Examples:
--------

    $ ./pdbwhois.py 2001:7f8:4::ede3:1
    aTech Media - AS60899 is peering at LINX Juniper LAN on 2001:7f8:4::ede3:1

    $ ./pdbwhois.py 195.66.224.244
    Astutium Ltd - AS29527 is peering at LINX Juniper LAN on 195.66.224.244

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
    
    Facility Name: Linxdatacenter (Warsaw)

    $ pdb --ix lon1
    Internet Exchange: LINX LON1
        city: London
        country: GB
        website: https://www.linx.net/
        tech_phone: +44 20 76453500
        IPv4: 195.66.224.0/22
        IPv4: 195.66.230.0/26
        IPv6: 2001:7f8:4::/64

    $ pdb --ix lon1 -v
    Internet Exchange: LINX LON1
        city: London
        country: GB
        website: https://www.linx.net/
        tech_phone: +44 20 76453500
        IPv4: 195.66.224.0/22
        IPv4: 195.66.230.0/26
        IPv6: 2001:7f8:4::/64
    Networks Present:
        Swisscom - AS3303
        GTT Communications (AS3257) - AS3257
        Renesys - AS64597
        Telecom Italia Sparkle - AS6762
        Level3 formerly Global Crossing - AS3549
        Easynet Global Services - AS4589
        NetCologne - AS8422
        Global Cloud Xchange (f.k.a. FLAG Telecom) - AS15412
        Timico Limited - AS8607
        RCS & RDS - AS8708
        Claranet - AS8426
        Free SAS - AS12322
        sunrise, TDC Switzerland AG - AS6730
        RETN - AS9002
    ...
    
    
    $ pdb --fac LD5 -v
    Facility Name: Equinix London Slough (LD5)
    Networks:
        Equinix UK - AS21371
        Oracle RightNow - AS15179
        Smoothstone/West IP Communications - AS32880
        Nuco Technologies Ltd - AS45014
        Nuco Technologies Ltd - AS33854
        Exponential-e Ltd - AS25180
        UK Webhosting Ltd - AS198047
        EE - AS12576
        IX Reach - IIX - AS43531
    ...