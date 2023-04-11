from socket import *

port = 5050
server = "192.168.137.26"
server_name = gethostname()
server_socket = socket(AF_INET, SOCK_STREAM)
addr = (server, port)
server_socket.bind(addr)
server_socket.listen()
print(f"This is server of {server_name}")
print("I am listening")
while True:
    connection, adderss = server_socket.accept()
    recieve = connection.recv(1024).decode()
    recieve_list = recieve.split(",")
    if int(recieve_list[1]) <= 100 and int(recieve_list[1]) >= 0:
        num = 100
        print(f"this is client {recieve_list[0]}")
        print(f"the number choosen by the client is {recieve_list[1]}")
        print(f"the number choosen by sew is {num}")
        print(f"their sum is {num + int(recieve_list[1])}")
        send_data = f"{server_name},{num}"
        connection.send(send_data.encode())
        connection.close()
    else:
        send_data = "invalid input"
        connection.send(send_data.encode())
        connection.close()
        break