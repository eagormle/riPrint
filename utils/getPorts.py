import socket

def scan_ports(ip_address, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        try:
            # Create a new socket for each port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set a timeout for attempting to connect
            result = s.connect_ex((ip_address, port))
            s.close()
            # If connect_ex returns 0, the port is open
            if result == 0:
                open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {str(e)}")
    return open_ports

def display_open_ports(ip_address, open_ports):
    if open_ports:
        print(f"Open ports on {ip_address}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip_address}.")

if __name__ == "__main__":
    target_ip = "192.168.1.35"  # Replace with the IP address you want to scan
    port_range = [631, 632]  # Replace with the range of ports you want to scan
    open_ports = scan_ports(target_ip, port_range)
    display_open_ports(target_ip, open_ports)


# [515, 9100, 5357, 631] are common ports for epson