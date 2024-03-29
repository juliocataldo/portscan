#!/usr/bin/python
import socket
import sys
import os
import requests

'''
THIS IS MY FIRST EXPERIENCE CODING SOMETHING USEFULL IN PYTHON.
I INTEND TO USE THIS CODE FOR CYBERSECURITY STUDYING ONLY.
ITS A BASIC AND VERY SIMPLE PROJECT AND OPEN SOURCE.
************* 
Once you input the host name, it will give you the IP address, then
it will scann for all open ports and, finally, print a banner for each 
detected open port.
'''

print ("\n\n\n=============****   PYTHON PORT SCAN  ****=============")
print ("=============****  INSERT YOUR HOST AND WAIT ****=============")
print ("=============************************************=============\n")

host = input("\n Please, insert the host name ---> ")
ip1 = socket.gethostbyname(host)

open_ports = []

print ("\n************ The host ip address is: ", ip1, "\n")
print ("\n ---->Now let me scan the juice out of it!")
print ("==============================================\n")

for port in range (1, 65535):
    mysocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    if (mysocket.connect_ex ((ip1,port)) == 0):
        open_ports.append(port)
        site = requests.get("http://"+host)
        status = site.status_code
        print ("Port ", port, "is OPEN, and the Status is: ", status)
        mysocket.close()
print ("\n ---->Now let me show you the banners for each open port!")
print ("==============================================\n")

for x in open_ports:
    mynewsocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    mynewsocket.connect((ip1,x))
    banner = mynewsocket.recv(1024)
    mynewsocket.close()
    print ("\nFor Port number ",x,"The banner is: ",banner,"<---")
