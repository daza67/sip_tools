#!/usr/bin/python

import socket

R_IP = input('Enter the phone IP?\n')
## R_IP = '192.168.152.2'
R_PORT = 5060 

message = 'NOTIFY sip:810@local;transport=udp SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.1.1:5060;branch=z9hG4bKpq4vtg301gl7a6vu02f0.1\r\nFrom: <sip:192.168.1.1>;tag=1619158584-1690860757051-\r\nTo: <sip:810@local>\r\nCall-ID: WB1332370510108231369901025@192.168.1.1\r\nCSeq: 395563037 NOTIFY\r\nContact: <sip:192.168.1.1:5060;transport=udp>\r\nEvent: check-sync\r\nSubscription-State: terminated\r\nMax-Forwards: 69\r\n\r\nContent-Length: 0'
def sendPacket():
   proto = socket.getprotobyname('udp')                         
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto)

   try:
       s.connect((R_IP , R_PORT)) 
       s.sendall(message.encode())                                       
   except socket.error:
       pass
   finally:
       s.close()

sendPacket()