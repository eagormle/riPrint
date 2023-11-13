import socket
import threading

def establish_connection(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=10) as sock:
            print(f"Connected to {ip}:{port}")
            while True:
                pass  # Keep the connection open
    except Exception as e:
        print(f"Error connecting to {ip}:{port}: {e}")

def create_dummy_connections(ip, port, number_of_connections):
    threads = []
    for _ in range(number_of_connections):
        thread = threading.Thread(target=establish_connection, args=(ip, port))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()  # Optionally wait for threads to finish

if __name__ == "__main__":
    printer_ip = "192.168.1.35"  # Replace with the actual IP address of the printer
    printer_port = 9100  # Common port for IPP
    number_of_dummy_connections = 5  # Specify the number of dummy connections

    try:
        print(f"Establishing {number_of_dummy_connections} connections to {printer_ip}:{printer_port}")
        create_dummy_connections(printer_ip, printer_port, number_of_dummy_connections)
    except KeyboardInterrupt:
        print("Interrupted, closing connections...")
