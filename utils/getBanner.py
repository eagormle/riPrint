import socket

# Dictionary mapping printer languages to common manufacturers
printer_languages = {
    'PJL': ['HP', 'Lexmark', 'Canon'],
    'PCL': ['HP', 'Canon', 'Brother'],
    'PostScript': ['HP', 'Canon', 'Epson', 'Xerox'],
    'ESC/P': ['Epson'],
    'IPP': ['HP', 'Canon', 'Epson', 'Brother', 'Lexmark']
}

def grab_banner(ip_address, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Set a timeout to prevent hanging
        s.connect((ip_address, port))  # Connect to the device
        
        # Receive data (the banner)
        banner = s.recv(1024)
        s.close()
        return banner.decode('utf-8', errors='replace')
    except Exception as e:
        print(f"Could not connect to {ip_address}:{port} - {str(e)}")
        return None
    
def analyze_banner(banner):
    # Check if banner contains common printer-related terms
    printer_keywords = ['printer', 'ipp', 'pcl', 'laserjet', 'deskjet', 'epson', 'xerox', 'brother', 'lexmark', 'canon']
    for keyword in printer_keywords:
        if keyword.lower() in banner.lower():
            return keyword  # Return the matching keyword
    return None

def get_printer_languages(manufacturer):
    languages = []
    for language, manufacturers in printer_languages.items():
        if manufacturer in manufacturers:
            languages.append(language)
    return languages

# This will need to be refactored, decision matrix is proof of concept
def scan_for_printers(ip_list):
    printer_ports = [9100, 515, 5357, 631]
    for ip_address in ip_list:
        for port in printer_ports:
            banner = grab_banner(ip_address, port)
            if banner:
                print(f"Banner on {ip_address}:{port}:\n{banner}")
                manufacturer_keyword = analyze_banner(banner)
                if manufacturer_keyword:
                    print(f"The device at {ip_address}:{port} is likely a printer.")
                    languages = get_printer_languages(manufacturer_keyword)
                    if languages:
                        print(f"Common printer languages used by {manufacturer_keyword}: {', '.join(languages)}\n")
                    else:
                        print(f"No common printer languages found for {manufacturer_keyword}.\n")

if __name__ == "__main__":
    # Assume you have a list of IP addresses to scan
    ip_list = ['192.168.1.35']
    scan_for_printers(ip_list)

   # [515, 9100, 5357, 631]