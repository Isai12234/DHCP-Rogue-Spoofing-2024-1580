# DHCP Rogue / Spoofing Attack - Scapy

## Autor
Nombre: Isai Casado
Matrícula: 2024-1580

---

## Objetivo
Desarrollar un script en Python utilizando Scapy para simular un servidor DHCP falso que responde a solicitudes DHCP Discover con una configuración maliciosa.

---

## Topología
- 1 Router
- 1 Switch
- 1 Host Atacante (Kali Linux)
- 1 Host Víctima (Window 10)

### Direccionamiento IP
Red: 10.15.80.0/24
Atacante: 10.15.80.3
IP Ofrecida: 10.15.80.20

---

## Parámetros utilizados
- Interfaz: ens3
- Python 3
- Scapy

---

## Ejecución
sudo python3 dhcp_rogue.py

---

## Medidas de mitigación
- DHCP Snooping
- Port Security
- Segmentación VLAN
- 802.1X
