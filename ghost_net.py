import scapy.all as scapy

def scan(ip):
    # Create an ARP request to ask "Who has this IP?"
    arp_request = scapy.ARP(pdst=ip)
    # Create a Broadcast packet to send it to everyone on the network
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    # Send the packet and get the responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

# Replace '192.168.1.1/24' with your actual network range
# You can find your IP by typing 'ifconfig' in terminal
scan("192.168.1.1/24")