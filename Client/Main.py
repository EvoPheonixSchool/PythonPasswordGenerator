#this class is the client that sends options to the server for a password
import socket

s = socket.socket()
host = socket.gethostname()
port = 8081
s.connect((host, port))
#print s.recv(1024)

#Ask for user input on password and send to server
length = input("Enter a password length:")
s.send(str(length))
symbols = raw_input("Would you like symbols?(y/n)")
s.send(symbols)
capitals = raw_input('Would you like Capitals?(y/n')
s.send(capitals)
spaces = raw_input('Would you like spaces?(y/n)')
s.send(spaces)

print(s.recv(1024))
