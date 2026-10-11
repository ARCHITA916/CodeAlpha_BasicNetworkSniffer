# Basic Network Sniffer

## Overview

A basic network sniffer developed using Python and Scapy as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and displays useful information such as source and destination IP addresses, protocols, port numbers, packet payload size, payload preview, and capture time.

## Objectives

- Understand how network packets travel between devices.
- Learn the basic structure of IP packets.
- Identify common network protocols.
- Practice packet capture and analysis using Python.

## Features

- Captures multiple network packets using Scapy.
- Displays source and destination IP addresses.
- Identifies TCP, UDP, and ICMP protocols.
- Displays source and destination ports when available.
- Calculates the size of raw packet payloads.
- Displays a preview of up to 50 bytes of raw payload when available.
- Records the time when each packet is processed.

## Technologies Used

- Python
- Scapy
- Npcap
- Visual Studio Code
- Git and GitHub

## How It Works

1. Imports the required Python and Scapy modules.
2. Captures network packets.
3. Checks whether a packet contains an IP layer.
4. Extracts source and destination IP addresses.
5. Identifies the network protocol.
6. Extracts TCP or UDP port numbers when available.
7. Calculates the raw payload size and displays a short preview when available.
8. Prints the analyzed packet information.

## Requirements

- Python installed on your computer.
- Scapy Python library.
- Npcap installed on Windows when required for packet capture.
- Appropriate permissions to capture network traffic.

## Installation

### 1. Install Python

Download Python from https://www.python.org/downloads/ and follow the installation instructions.

### 2. Install Npcap

On Windows, install Npcap from https://npcap.com/ if required for your network adapter and Scapy configuration.

### 3. Install Scapy

Open PowerShell or Command Prompt and run:

```bash
python -m pip install scapy
```

### 4. Download the Project

Clone the repository:

```bash
git clone https://github.com/ARCHITA916/CodeAlpha_BasicNetworkSniffer.git
```

Move into the project folder:

```bash
cd CodeAlpha_BasicNetworkSniffer
```

## Run the Program

Run the following command from the project folder:

```bash
python packet_info.py
```

The program attempts to capture up to 20 packets and displays the analyzed information. Packet capture may require running the terminal with appropriate permissions and selecting a supported network interface.

## Ethical Use and Limitations

Use this tool only on your own network or on networks for which you have explicit authorization to monitor traffic.

The payload preview may contain sensitive information. The program displays only a short preview and does not decode every protocol or capture every possible packet type. Packets without an IP layer are ignored.

## Learning Outcome

This project provides introductory hands-on experience with Python, packet capture, network protocols, and basic network traffic analysis.

Developed as part of the CodeAlpha Cyber Security Internship.
