import ipp
import socket
from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo

class MyListener:
    def __init__(self):
        self.printers = []

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            addresses = socket.inet_ntoa(info.addresses[0])
            self.printers.append({'name': name, 'ip': addresses, 'port': info.port})

def discover_printers():
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_ipp._tcp.local.", listener)
    try:
        input("Press Enter after printers are discovered...")
    finally:
        zeroconf.close()
    return listener.printers

def send_blank_job(printer_ip, printer_port, num_jobs):
    for _ in range(num_jobs):
        client = ipp.Client(f"http://{printer_ip}:{printer_port}/ipp/print")
        job = client.create_job()
        client.send_document(job, b"", "application/octet-stream", last_document=True)
        print(f"Sent blank job to {printer_ip}:{printer_port}")

if __name__ == "__main__":
    printer_ip = "192.168.1.100"  # Replace with a printer ip address
    printer_port = 631  # Common port for IPP
    num_jobs = 5  # Number of blank print jobs to send

    send_blank_job(printer_ip, printer_port, num_jobs)
