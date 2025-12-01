import socket
import sys
from datetime import datetime

# Define the target (The IP you want to scan)

target = "scanme.nmap.org"

# Add a pretty banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # Scan ports 1 to 100 (You can increase this to 1000 or 65535)
    for port in range(1, 100):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout so it doesn't hang if a port is unresponsive
        s.settimeout(1)

        # Try to connect to the port (returns 0 if successful)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        # Close the connection
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()

print("-" * 50)
print("Scan completed.")
