import socket
import thread

from Server.Generate import Generate


class Connection:

    def connect(self, list):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8081
        s.bind((host, port))
        while True:
            s.listen(5)
            client, address = s.accept()
            gen = Generate()
            thread.start_new_thread(gen.start, (client, list))


