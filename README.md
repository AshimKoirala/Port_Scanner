# 🔎 Python Port Scanner ( Inspired by Nmap )

A simple TCP-based port scanner built using Python's socket library.

## 📌 Description
This project is a basic TCP port scanner written in Python using the built-in socket library.  
It attempts to establish TCP connections to a list of common ports on a target system to determine which ports are open.

## ▶️ How to Run

1. Clone the repository:

   ``` bash
    git clone https://github.com/AshimKoirala/Port_Scanner.git


2. Navigate to the folder:

   ```bash
   cd Port_Scanner

3. Run the script:

   ```bash
   python port_scanner.py

4. Enter target IP or domain when prompted.


## 🖥 Example Output

Enter target IP or domain : scanmap.nmap.org

Port 22 is OPEN
Port 80 is OPEN

Scan completed

### 🔍 What Happens Behind the Scenes?

1. A TCP socket is created.
2. The program attempts to connect to a target port.
3. The operating system performs the TCP three-way handshake:
   SYN → SYN/ACK → ACK
4. If the connection succeeds, the port is considered open.
5. The connection is closed and the next port is tested.


## 🚀 Features
- Uses socket programming
- Scans common TCP ports
- Identifies open ports

## ⚠ Disclaimer
This tool is for educational purposes only.
Do not scan systems without permission.


## 👤 Author
Ashim


