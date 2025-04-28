import argparse
from scapy.all import ARP, Ether, srp
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style
import pyfiglet
import warnings

# Suppress warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

# Create a console instance
console = Console()

# Function to display the banner using pyfiglet
def display_banner():
    banner = pyfiglet.figlet_format("SCAN MAC")
    print(f"{Fore.BLUE}{banner}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Developed by: Ben Mansour Ahmed{Style.RESET_ALL}\n")

# Function to perform the ARP scan
def run_scan(ip_or_range):
    dst_bc = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC
    arp_header = ARP(pdst=ip_or_range)
    all_packet = dst_bc / arp_header

    # Send packet and receive responses
    result, noresult = srp(all_packet, timeout=2, verbose=False)

    # Create a table to display results
    table = Table(title=f"Live Hosts in {ip_or_range}")
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")

    # Populate the table with the results
    for sent, received in result:
        table.add_row(received.psrc, received.hwsrc)

    # Print the table
    console.print(table)

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Scan MAC Addresses in a network")
    parser.add_argument("-i", "--ip", required=True, help="IP range or address to scan")
    args = parser.parse_args()

    # Display the banner
    display_banner()

    # Run the scan with the provided IP range
    run_scan(args.ip)

if __name__ == "__main__":
    main()
