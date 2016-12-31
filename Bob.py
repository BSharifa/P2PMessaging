from socket import *
from pyDes import *
import Tkinter as tk
import random
import getpass
import sys



#ask for the password for the connection
#password = raw_input("Please provide the password: ")
password = '1234'
pass_try = 0
x = 3

while pass_try < x:
    user_input = getpass.getpass("Please provide the password: ")
    if user_input != password:
        pass_try += 1
        print 'Incorrect Password, ' + str(x-pass_try) + ' more attempts left\n'
    else:
        pass_try = x + 1
 
if pass_try != x and user_input == password:
        


#password = getpass.getpass("Please provide the password: ")

#if password == '123':

    #provide the host name and port no
    HOST = ''#'' #localhost / 192.168.1.1
    PORT = 8099

    #use the password as a seed for the random number generation
    random.seed(int(password))

    #setup the connection
    s = socket(AF_INET, SOCK_STREAM)# 98% of all socket programming will use AF_INET and SOCK_STREAM
    s.bind((HOST, PORT))
    s.listen(1) # how many connections it can receive at one time
    conn, addr = s.accept() # accept the connection
    print 'Connected by', addr # print the address of the person connected


    #the following part is for message send and receive
    while True:
        data = conn.recv(1024) #recives datae (1024 bytes) using conn and store into data
        #select a random key which should be 8 bit so the range of the random number generation should be 8 character long
        key = random.randint(10000000,90000000)
        #define the encrypt and decrypt process using the key
        k = des(str(key), CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        data1= k.decrypt(data)
        print "Received from Alice: ", repr(data1),repr(data) # print data; Data is the message the users types
        reply = raw_input("Bob: ")
        reply1= k.encrypt(reply)
        conn.sendall(reply1)
        print "Send encrypted data: ", repr(reply1)
    conn.close()
else:
    sys.exit('You have provided wrong password!!! terminating... \n')
    


