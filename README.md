# Ghost-Net 📡

A low-level local network discovery and host inventory tool that uses raw ARP packet crafting to map active devices across subnets.

## What It Does
Ghost-Net broadcasts crafted Layer 2 Ethernet frames (`ff:ff:ff:ff:ff:ff`) containing ARP requests (`"Who has IP X.X.X.X? Tell me"`) across the local subnet. It captures incoming ARP replies to construct an up-to-date mapping of live IPv4 addresses and hardware MAC addresses without relying on passive OS caches.

## Why I Built It
Standard ICMP ping sweeps (`ping -c 1`) are frequently ignored or blocked by modern OS firewalls. ARP operates at the data link layer and cannot be dropped by endpoint software firewalls on local subnets. I built Ghost-Net to explore raw packet crafting with Scapy and understand network host discovery at the protocol level.

## Tech Stack
- **Language:** Python 3.x
- **Networking Library:** [Scapy](https://scapy.net/) (`scapy.all`)
- **Protocols:** Layer 2 Ethernet (`Ether`), Address Resolution Protocol (`ARP`)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/PS282006/Ghost-Net.git
   cd Ghost-Net
   ```
2. Install Scapy:
   ```bash
   pip install scapy
   ```
3. Run with root/superuser privileges (required for raw packet socket access):
   ```bash
   sudo python3 ghost_net.py
   ```
   *Note: On macOS, ensure terminal has permissions to access network interfaces (e.g., `en0`).*
