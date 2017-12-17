# this class creates the connection and thread for each client
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
import socket
import thread

from Server.Generate import Generate


class Connection:
    # This class is used to create a connection to a client and thread for them
    def connect(self, list):
        # sets socket to lisen on
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8081
        s.bind((host, port))
        # wait for connection and create a new thread for each client
        while True:
            s.listen(5)
            client, address = s.accept()
            gen = Generate()
            # creates thread
            thread.start_new_thread(gen.start, (client, list))
