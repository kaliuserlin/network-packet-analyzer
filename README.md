# Network Packet Analyzer

A Python-based network packet sniffer and traffic analyzer developed as a cybersecurity minor project.

## Project Overview

This project captures and analyzes network packets in real time using Python and Scapy. It identifies common protocols, displays source and destination IP addresses, records port information, calculates packet statistics, saves packet information to CSV, supports protocol filtering, and generates traffic visualizations.

The project was developed and tested in a controlled Kali Linux virtual machine environment.

## Features

- Live network packet capture
- TCP packet detection
- UDP packet detection
- ICMP packet detection
- Source IP identification
- Destination IP identification
- Source and destination port detection
- Packet size calculation
- Timestamp recording
- CSV packet logging
- Protocol statistics
- Total traffic calculation
- Average packet size calculation
- TCP/UDP/ICMP filtering
- Protocol distribution visualization
- Packet size distribution visualization

## Technologies Used

- Python 3
- Scapy
- Matplotlib
- CSV
- Kali Linux
- VirtualBox

## Project Structure

```text
network-packet-analyzer/
│
├── data/
│   ├── protocol_distribution.png
│   └── packet_size_distribution.png
│
├── sniffer.py
├── visualize.py
├── README.md
└── .gitignore

The Python virtual environment is intentionally excluded from the GitHub repository.

How It Works

The packet analyzer listens on the selected network interface and processes IPv4 packets.

For each packet, the program extracts:

Time
Source IP
Destination IP
Protocol
Source Port
Destination Port
Packet Size

The captured information is displayed in the terminal and written to a CSV file.

Example Output
TIME     | SOURCE          -> DESTINATION     | PROTO | PORT | SIZE
---------------------------------------------------------------------------
08:21:14 | 10.0.2.15      -> 8.8.8.8         | ICMP  | - -> - | 98 bytes
08:21:15 | 10.0.2.15      -> 10.219.222.149  | UDP   | 45321 -> 53 | 71 bytes
08:21:16 | 10.0.2.15      -> 172.66.147.243  | TCP   | 51234 -> 80 | 60 bytes
Running the Packet Sniffer

Activate the virtual environment:

source venv/bin/activate

Run the analyzer:

sudo ./venv/bin/python sniffer.py

The program continuously captures packets until Ctrl+C is pressed.

Protocol Filtering

The analyzer supports protocol-specific filtering.

Capture all supported traffic
sudo ./venv/bin/python sniffer.py
Capture TCP traffic
sudo ./venv/bin/python sniffer.py tcp
Capture UDP traffic
sudo ./venv/bin/python sniffer.py udp
Capture ICMP traffic
sudo ./venv/bin/python sniffer.py icmp

This allows individual protocols to be analyzed separately.

Traffic Statistics

When the capture is stopped, the program displays:

Total packets analyzed
TCP packet count
UDP packet count
ICMP packet count
Other packet count
Total captured data
Average packet size

Example:

========================================
Capture stopped. Packets analyzed: 29
========================================
Total packets : 29
TCP packets : 11
UDP packets : 10
ICMP packets : 8
OTHER packets : 0
Total data : 3444 bytes
Average size : 118.76 bytes
----------------------------------------
CSV file saved: data/packets.csv
========================================
CSV Logging

Packet information is saved to:

data/packets.csv

The CSV contains the following fields:

Time
Source IP
Destination IP
Protocol
Source Port
Destination Port
Packet Size

The live CSV file is excluded from the GitHub repository because it contains locally captured network traffic.

Visualization

The project includes a separate visualization program called:

visualize.py

Run it using:

python visualize.py

The program generates two charts.

Protocol Distribution
data/protocol_distribution.png

This chart displays the number of captured packets for each supported protocol.

Packet Size Distribution
data/packet_size_distribution.png

This chart shows the distribution of packet sizes observed during the capture.

Testing

The project was tested in a controlled Kali Linux virtual machine.

The following types of traffic were generated and analyzed:

ICMP traffic using ping
UDP/DNS traffic
TCP/HTTP traffic using curl
Mixed network traffic
Protocol-specific traffic using filtering

The analyzer successfully captured packet information, logged traffic, calculated statistics, and generated visualizations.

Learning Outcomes

This project provided practical experience with:

Network packet analysis
TCP/IP networking
Network protocols
IP addressing
TCP and UDP ports
ICMP traffic
Python programming
Scapy
Linux networking
CSV data processing
Network traffic statistics
Data visualization
Basic cybersecurity monitoring
Limitations

This is an educational network packet analyzer rather than a complete enterprise security monitoring system.

Current limitations include:

Limited protocol support
IPv4-focused analysis
No deep packet inspection
No automated threat detection
No intrusion detection rules
No database backend
No web dashboard
No automated security alerts
Future Scope

The project can be expanded into a more advanced Network Intrusion Detection and Security Monitoring System.

Possible future improvements include:

Intrusion detection
Port scan detection
Suspicious traffic detection
Anomaly detection
Security alerts
IP reputation checking
Database storage
Real-time monitoring dashboard
Advanced protocol analysis
Automated log analysis
Snort or Suricata integration
Ethical Use

This project should only be used on networks and systems where you have permission to capture and analyze traffic.

Packet capture may contain sensitive information, so testing should be performed only in an authorized environment such as a personal laboratory, virtual machine, or permitted network.

Project Status

Completed features:

Live packet capture
Protocol identification
IP and port extraction
CSV logging
Traffic statistics
Protocol filtering
Packet size analysis
Traffic visualization

Future development:

Network intrusion detection
Automated security alerts
Real-time monitoring dashboard
Advanced security analysis
Author

Kaliuserlin

Cybersecurity Minor Project
