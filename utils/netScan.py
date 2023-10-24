import scapy.all as scapy

def scan(ip_range):
    # Create an ARP request packet to get MAC addresses for the IP range
    arp_request = scapy.ARP(pdst=ip_range)
    
    # Create an Ethernet frame to send the ARP request
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    
    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = ether/arp_request
    
    # Send the packet and capture responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # Extract IP and MAC addresses from responses
    devices_list = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)
    return devices_list

def display_results(devices_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices_list:
        print(device["ip"] + "\t\t" + device["mac"])

if __name__ == "__main__":
    target_ip_range = "192.168.1.1/24"  # Replace with your local network IP range
    devices = scan(target_ip_range)
    display_results(devices)
