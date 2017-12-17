# this class generates the password and sends it off
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
import re
from random import randint


class Generate(object):
    pass


class Generate:
    list = []

    # Ask for user input on password
    def start(self, client, list):
        print("Connection made")
        length = int(client.recv(1024))
        symbols = client.recv(1024)
        capitals = client.recv(1024)
        spaces = client.recv(1024)

        # create string to requested length
        password = list[randint(0, len(list) - 1)]
        while (len(password) < length):
            password += list[randint(0, len(list) - 1)]

        # logic for handling is spaces are needed
        if (spaces == "n"):
            password = password.replace(" ", "")
            while (len(password) < length):
                # fills in password space to meet length requirements
                password += list[randint(0, len(list) - 1)]
                password = password.replace(" ", "")

        # logic for replacing special characters
        if (symbols == "n"):
            password = re.sub('[^a-zA-Z0-9\n\.]', '', password)
            while (len(password) < length):
                # fills in password space to meet length requirements
                password += list[randint(0, len(list) - 1)]
                password = password.replace(" ", "")
                password = re.sub('[^a-zA-Z0-9\n\.]', '', password)

        # remove capitals
        if (capitals == "n"):
            password = password.lower()

        password = password[0: length]

        # sends the password to the client
        client.send(("Password: ") + password)
        print "Password sent"
