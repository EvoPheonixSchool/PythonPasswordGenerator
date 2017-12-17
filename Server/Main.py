# this is the main class to controll the password generator
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
from OpenFile import OpenFile
from Connection import Connection


#creates an object of the openfile class
oFile = OpenFile()
conn = Connection()
list = []
password = ""

#creates a file object from the file made in the openfile class
#passing the filename and mode to use
file = oFile.open("00010014-eng.csv", "r+")

# printing my name
print("Sheldon McGrath")
print("Waiting for Connections...")

#gets a list of EST values stripped from the file
list = oFile.StripEST(file)

conn.connect(list)


