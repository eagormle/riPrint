import nmap
import logging
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from zeroconf import ServiceBrowser, Zeroconf

# Setup logging
log_file_handler = logging.FileHandler('summary.log', mode='w')
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_file_handler)
# Dictionary mapping printer languages to common manufacturers
printer_languages = {
    'PJL': ['HP', 'Lexmark', 'Canon'],
    'PCL': ['HP', 'Canon', 'Brother'],
    'PostScript': ['HP', 'Canon', 'Epson', 'Xerox'],
    'ESC/P': ['Epson'],
    'IPP': ['HP', 'Canon', 'Epson', 'Brother', 'Lexmark']
}

class MyListener:
    def remove_service(self, zeroconf, type, name):
        logging.info(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        logging.info(f"Service {name} added, service info: {info}")

def grab_banner(ip_address, port):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip_address, arguments=f'-p {port} -sV --script=default --max-retries 1 --host-timeout 30s')
        service_info = nm[ip_address].get('tcp', {}).get(port, {})
        if service_info:
            return f"{service_info.get('name', 'Unknown')} ({service_info.get('product', 'Unknown')})"
        else:
            logging.info(f"No service information found on {ip_address}:{port}")
            return None
    except nmap.PortScannerError as e:
        logging.error(f"PortScannerError on {ip_address}:{port} - {str(e)}")
        return None
    except KeyError:
        # Ignore KeyError exceptions
        return None

def analyze_banner(banner):
    printer_keywords = ['printer', 'ipp', 'pcl', 'laserjet', 'deskjet', 'epson', 'xerox', 'brother', 'lexmark', 'canon']
    for keyword in printer_keywords:
        if keyword.lower() in banner.lower():
            return keyword
    return None

def get_printer_languages(manufacturer):
    languages = []
    for language, manufacturers in printer_languages.items():
        if manufacturer in manufacturers:
            languages.append(language)
    return languages

def scan_ip(ip_address):
    printer_ports = [9100, 515, 5357, 631]
    result_data = {'ip_address': ip_address, 'printers': []}
    for port in printer_ports:
        banner = grab_banner(ip_address, port)
        if banner:
            printer_data = {
                'port': port,
                'banner': banner,
            }
            manufacturer_keyword = analyze_banner(banner)
            if manufacturer_keyword:
                printer_data['manufacturer'] = manufacturer_keyword
                languages = get_printer_languages(manufacturer_keyword)
                if languages:
                    printer_data['languages'] = languages
                else:
                    printer_data['languages'] = 'Unknown'
            result_data['printers'].append(printer_data)
    # Only log the result if printers were found
    if result_data['printers']:
        logging.info(result_data)

def print_summary():
    with open('summary.log', 'r') as log_file:
        log_content = log_file.read()
    print(log_content)

if __name__ == "__main__":
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_ipp._tcp.local.", listener)
    try:
        ip_list = ['192.168.1.' + str(i) for i in range(1, 40)]
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(scan_ip, ip_list)
    finally:
        zeroconf.close()
    print_summary()
