from pysnmp.hlapi import *

def try_community_string(ip, community_string):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community_string),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))  # OID for sysDescr
               )
    )
    if errorIndication or errorStatus:
        return None  # SNMP request failed
    else:
        return community_string  # SNMP request succeeded

def brute_force_community_string(ip, community_strings):
    for community_string in community_strings:
        success = try_community_string(ip, community_string)
        if success:
            return community_string
    return None

def get_snmp_data(ip, oid, community_string='private'):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community_string),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )
    if errorIndication or errorStatus or not varBinds:
        print(f"Failed to retrieve data with community string '{community_string}'. Attempting brute force...")
        community_strings = ["public", "private", "community", "snmp"]  # List of community strings to try
        working_community_string = brute_force_community_string(ip, community_strings)
        if working_community_string:
            print(f"Found working community string: {working_community_string}")
            # Retry the SNMP request with the working community string
            return get_snmp_data(ip, oid, working_community_string)
        else:
            print("No working community string found.")
            return None
    else:
        for varBind in varBinds:
            print(f'{varBind[0].prettyPrint()} = {varBind[1].prettyPrint()}')

# Example usage:
ip_address = '192.168.1.35'  # Replace with your printer's IP address
oid = '1.3.6.1.2.1.1.1.0'  # OID for sysDescr
get_snmp_data(ip_address, oid)
