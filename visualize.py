import csv
import matplotlib.pyplot as plt

csv_file = "data/packets.csv"

protocol_counts = {
  "TCP":0,
  "UDP":0,
  "ICMP":0,
  "OTHER":0
}

packet_sizes = []

with open(csv_file, "r") as file:
 reader = csv.DictReader(file)

 for row in reader:
  protocol = row["Protocol"]

  if protocol in protocol_counts:
   protocol_counts[protocol] += 1

  packet_sizes.append(int(row["Packet Size"]))

#protocol distribution
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())

plt.figure()
plt.bar(protocols, counts)
plt.title("Network Traffic by Protocol")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.tight_layout()
plt.savefig("data/protocol_distribution.png")

#packet size distribution
plt.figure()
plt.hist(packet_sizes, bins=10)
plt.title("Packet Size Distribution")
plt.xlabel("Packet Size (bytes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("data/packet_size_distribution.png")
print("Visualization complete.")
print("Charts saved in data/")
