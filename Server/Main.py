import re

from OpenFile import OpenFile
from random import randint
from Connection import Connection
#this is the main class to controll the password generator

#creates an object of the openfile class
oFile = OpenFile()
conn = Connection()
list = []
password = ""

#creates a file object from the file made in the openfile class
#passing the filename and mode to use
#file = oFile.open("also test.txt", "r+")
file = oFile.open("test.csv", "r+")

#gets a list of EST values stripped from the file
list = oFile.StripEST(file)

conn.connect(list)
#client.send("test")

#prints the file for testing
#print(file.read())


