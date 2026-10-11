# 🛡️ Basic Network Sniffer

A Python-based network packet analyzer developed as part of the **CodeAlpha Cyber Security Internship**. This project demonstrates the fundamentals of packet capture, network protocols, and basic traffic analysis using Scapy.

## 📌 Project Overview

The Basic Network Sniffer captures network packets and displays essential packet information, including source and destination IP addresses, protocol types, port numbers, payload size, and a short payload preview when available.

This project provides hands-on experience with fundamental networking concepts and Python-based packet analysis.

## 🎯 Objectives

- Understand how data travels across computer networks.
- Explore the basic structure of IP packets.
- Identify common network protocols.
- Learn packet capture and analysis using Python and Scapy.
- Develop practical cybersecurity and networking skills.

## ✨ Features

- Captures up to 20 network packets.
- Displays source and destination IP addresses.
- Identifies TCP, UDP, and ICMP protocols.
- Displays source and destination port numbers when available.
- Calculates raw payload size when available.
- Displays a preview of up to 50 bytes of raw payload when available.
- Displays the time associated with each processed packet.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Scapy | Packet capture and analysis |
| Npcap | Packet capture support on Windows, when required |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## ⚙️ How It Works

1. Initializes the required Python and Scapy modules.
2. Captures network packets using Scapy.
3. Checks for the IP layer in each packet.
4. Extracts source and destination IP addresses.
5. Identifies the network protocol.
6. Retrieves TCP or UDP port numbers when available.
7. Checks for raw payload data and calculates its size.
8. Displays a short payload preview when available.
9. Prints the analyzed packet information in the terminal.

## 📋 Prerequisites

- Python installed on your system.
- Scapy Python library.
- Npcap on Windows, if required by your packet-capture configuration.
- Appropriate permissions to capture network traffic.

## 🚀 Installation and Setup

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/ARCHITA916/CodeAlpha_BasicNetworkSniffer.git
```

### 2. Navigate to the Project Directory

```bash
cd CodeAlpha_BasicNetworkSniffer
```

### 3. Install Scapy

```bash
python -m pip install scapy
```

### 4. Run the Program

```bash
python packet_info.py
```

**Note:** On Windows, install Npcap if required and run the terminal with appropriate permissions. Packet capture depends on your network adapter and Scapy configuration.

## 💻 Sample Output

The following is an illustrative example of the information displayed by the program:

```text
__________________________________________________
Time: 10:58:49
192.168.1.10 -> 192.168.1.20
Protocol: TCP
Source Port: 50817
Destination Port: 443
Payload Size: 0 bytes
Payload Preview: No raw payload
```

*Actual output will vary depending on the captured packets. A packet without a Raw layer may show “No raw payload.”*

## 🔐 Ethical Use and Limitations

This tool is intended for educational purposes and authorized network analysis only.

- Capture traffic only on your own device or networks you have permission to monitor.
- Packet contents may contain sensitive information.
- The tool does not decrypt HTTPS traffic.
- It provides basic packet information and does not perform comprehensive protocol decoding.
- Packets without an IP layer are ignored by the current implementation.

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and third-party libraries.
- Network packet capture using Scapy.
- IP addressing, TCP, UDP, and ICMP.
- Packet fields, ports, and raw payload inspection.
- GitHub-based project documentation and version control.

## 👩‍💻 Developer

**Archita B.**  
Second-Year B.Sc. Computer Science with Cyber Security Student

- **GitHub Profile:** https://github.com/ARCHITA916
- **Project Repository:** https://github.com/ARCHITA916/CodeAlpha_BasicNetworkSniffer

## 🏢 Internship

Developed as part of the **CodeAlpha Cyber Security Internship**.

This project represents a step in my ongoing journey of learning Python, computer networking, and cybersecurity through practical projects.

---

⭐ *If you find this project useful for learning, feel free to explore the repository.*

