Description
Scan MAC is a lightweight Python tool to scan a network and discover live hosts along with their MAC addresses.
It uses ARP requests to find active devices and displays the results in a colorful, easy-to-read table.

This tool is perfect for network administrators, penetration testers, or anyone who needs quick visibility into a local network.

🚀 Features
Perform ARP network scans with one command.

Display IP and MAC addresses in a beautiful Rich-style table.

Stylish ASCII art banner using pyfiglet.

Colorful terminal output for better readability.

📦 Requirements
Before running the script, install the required Python libraries:

pip install -r requirements.txt
Or install manually:


pip install scapy rich colorama pyfiglet
Required Libraries:

scapy

rich

colorama

pyfiglet

🛠️ How to Use
Clone the repository:

git clone https://github.com/ahmed252023/scan-mac.git
cd scan-mac
Install dependencies:

pip install -r requirements.txt
Run the scanner:


python scan_mac.py -i 192.168.1.0/24
Arguments:

-i, --ip: The IP address or network range to scan (example: 192.168.1.0/24).

Example command:

python scan_mac.py -i 10.0.0.1/24
