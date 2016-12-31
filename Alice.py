from socket import *
from pyDes import *
import Tkinter as tk
import random
import getpass
import sys
#ask for the password for the connection
#password = raw_input("Please provide the password: ")
#password = getpass.getpass("Please provide the password: ")

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
#if (password == '123'):

        #provide the host name and port no
    HOST = ''#'' #localhost / 192.168.1.1
    PORT = 8099
        #setup the connection
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # client-side, connects to a host
    #des = DES.new('01234567', DES.MODE_ECB)

         #use the password as a seed for the random number generation
    random.seed(int(password))

    while True:
        message = raw_input("Alice: ")
        #select a random key which should be 8 bit so the range of the random number generation should be 8 character long
        key = random.randint(10000000,90000000)
        #define the encrypt and decrypt process using the key
        k = des(str(key), CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        ciphertext = k.encrypt(message)
        s.send(ciphertext)
        print "Send encrypted data: ", repr(ciphertext)
        print "Awaiting reply"
        reply = s.recv(1024) # 1024 is max data that can be received
        dataa = k.decrypt(reply)
        print "Received  from Bob:", repr(reply), repr(dataa)

    s.close()
else:
    sys.exit('You have provided wrong password!!! terminating... \n')