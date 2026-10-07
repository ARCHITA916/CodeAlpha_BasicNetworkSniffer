# Basic Network Sniffer

## Overview

This project is a basic network sniffer developed in Python using the Scapy library.

The program captures network packets and analyzes basic packet information such as source IP address, destination IP address, protocol, port numbers, payload size, and capture time.

This project was developed as part of the CodeAlpha Cyber Security Internship.

## Objective

The main objective of this project is to understand how network packets are captured and how information is exchanged between devices over a network.

The project helps in learning the basic structure of network packets and identifying common protocols such as TCP, UDP, and ICMP.

## Features

- Captures network packets using Scapy
- Displays source and destination IP addresses
- Identifies common network protocols such as TCP, UDP, and ICMP
- Displays source and destination port numbers for TCP and UDP packets
- Shows the payload size of captured packets
- Displays the time at which each packet is captured
- Processes multiple packets during a single execution

## Technologies Used

- Python
- Scapy
- Npcap
- Visual Studio Code
- Git and GitHub

## How It Works

The program follows these basic steps:

1. Imports the required Scapy modules.
2. Defines a function to analyze each captured packet.
3. Checks whether the packet contains an IP layer.
4. Extracts the source and destination IP addresses.
5. Identifies the network protocol.
6. Extracts source and destination ports for TCP and UDP packets.
7. Checks whether the packet contains a payload and calculates its size.
8. Displays the analyzed packet information.
9. Captures multiple packets from the network for analysis.

## Installation

### 1. Install Python

Download and install Python on your system.

### 2. Install Scapy

Open PowerShell or Command Prompt and run:

```bash
python -m pip install scapy

git clone https://github.com/ARCHITA916/CodeAlpha_BasicNetworkSniffer.git

python packet_info.py
