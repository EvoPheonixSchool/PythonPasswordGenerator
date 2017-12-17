# this class is the client that sends options to the server for a password
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
import socket

# creating socket to server using local host
s = socket.socket()
host = socket.gethostname()
port = 8081
s.connect((host, port))

# print my name
print("Sheldon McGrath")

# Ask for user input on password and send to server
length = input("Enter a password length:")
s.send(str(length))
symbols = raw_input("Would you like symbols?(y/n)")
s.send(symbols)
capitals = raw_input('Would you like Capitals?(y/n')
s.send(capitals)
spaces = raw_input('Would you like spaces?(y/n)')
s.send(spaces)

# prints password from the server
print(s.recv(1024))
