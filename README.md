# Ghost-Net 📡
A lightweight network discovery tool built in Python using Scapy.

## Overview
Ghost-Net performs ARP scanning to discover active devices on a local network. It maps IP addresses to MAC addresses, providing a quick snapshot of network inventory.

## Features
- **ARP Request/Response:** Uses low-level packet crafting.
- **Fast Scanning:** Scans entire subnets in seconds.
- **Mac-Optimized:** Designed to run smoothly on Apple Silicon (M2).

## Requirements
`pip install scapy`

## Usage
`sudo python3 ghost_net.py`
*(Requires sudo for raw socket access)*