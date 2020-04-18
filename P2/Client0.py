import socket
import termcolor

class Client:
    def ping(self):
        print("OK!")

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def _str_(self):
        return f"Connection to server at {self.ip}, port: {self.port}"

    def debug_talk(self, msg_to_server):
        msg_from_server = self.talk(msg_to_server)
        print("To server: ", end="")
        termcolor.cprint(msg_to_server, "blue")
        print("From server: ", end="")
        termcolor.cprint(msg_from_server, "green")
        return msg_from_server

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        return response
