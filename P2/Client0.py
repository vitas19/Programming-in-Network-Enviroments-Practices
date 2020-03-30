import socket

class Client:
    def _init_(self, ip, port):
        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print("OK!")

    def _str_(self):
        return f"Connection to server at {self.ip}, port: {self.port}"

    def debug_talk(self, msg_to_server):
        msg_to_server = self.talk(msg_to_server)
        print("To server: ", end="")
        print("From server: ", end="")
        return msg_to_server

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        return response