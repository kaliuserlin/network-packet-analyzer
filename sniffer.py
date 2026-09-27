from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import os
import sys

filter_protocol = "ALL"
if len(sys.argv) > 1:
  filter_protocol = sys.argv[1].upper()
if filter_protocol not in ["ALL","TCP","UDP","ICMP"]:
  print("Invalid filter.")
  print("Use: all, tcp , udp , or icmp")
  sys.exit(1)
print(f"Filter : {filter_protocol}")
  
print("======================")
print("Network Packet Sniffer")
print("======================")
print("Interface : eth0")
print("Press Ctrl+c to stop.\n")

packet_count = 0
total_bytes = 0
protocol_stats = {
   "TCP":0,
   "UDP":0,
   "ICMP":0,
   "OTHER":0,
}
csv_file = "data/packets.csv"
os.makedirs("data", exist_ok=True)
with open(csv_file, "w", newline="") as file:
    writer=csv.writer(file)

    writer.writerow([
     "Time",
     "Source IP",
     "Destination IP",
     "Protocol",
     "Source Port",
     "Destination Port",
     "Packet Size"
])
    def process_packet(packet):
      global packet_count , total_bytes
 
      if IP in packet:

       timestamp = datetime.now().strftime("%H:%M:%S")
       source = packet[IP].src
       destination =packet[IP].dst
       packet_size = len(packet)

       if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
 
       elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

       elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

       else:
        protocol = "OTHER"
        source_port = "-"
        destination_port = "-"
       
       if filter_protocol != "ALL" and protocol!=filter_protocol:
         return
       packet_count += 1
       total_bytes += packet_size
       protocol_stats[protocol] += 1

       print(
        f"{timestamp} | "
        f"{source:<15} -> " 
        f"{destination:<15} | "
        f"{protocol:<5} | "
        f"{source_port:<5} -> " 
        f"{destination_port:<5}| "
        f"{packet_size} bytes"
       )
 
       writer.writerow([
        timestamp,
        source,
        destination,
        protocol,
        source_port,
        destination_port,
        packet_size
       ])
       file.flush()

    print(
        f"{'TIME':<8} | "
        f"{'SOURCE':<15} -> "
        f"{'DESTINATION':<15} | "
        f"{'PROTO':<5} | PORT | SIZE"
    )

    print("-" * 90)

    try:
        sniff(
         iface="eth0",
         prn=process_packet,
         store=False
       )
    finally:
      print("\n\n========================================")
      print(f"Capture stopped. Packets analyzed: {packet_count}")
      print("========================================")
      print(f"Total packets : {packet_count}")
      print(f"TCP packets : {protocol_stats['TCP']}")
      print(f"UDP packets : {protocol_stats['UDP']}")
      print(f"ICMP packets : {protocol_stats['ICMP']}")
      print(f"OTHER packets : {protocol_stats['OTHER']}")
      average_size = total_bytes / packet_count if packet_count > 0 else 0
      print(f"Total data : {total_bytes} bytes")
      print(f"Average size : {average_size:.2f} bytes")
      print("----------------------------------------")
      print(f"CSV file saved: {csv_file}")
      print("========================================")
