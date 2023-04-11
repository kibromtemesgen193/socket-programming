from socket import *

server_port = 5050
server_name = "10.5.214.103"
client_name = gethostname()
client_socket = socket(AF_INET, SOCK_STREAM)
server_address = (server_name, server_port)
number = input("please enter a number you choose form 1-100 \n")
num = int(number)
client_socket.connect(server_address)

while client_socket:
    send_list = f"{client_name},{number}"
    client_socket.send(send_list.encode())
    recieve = client_socket.recv(1024).decode()
    if recieve == "invalid input":
        print(recieve)
        break
    else:
        print(f"i am {client_name}")
        recieve_list = recieve.split(",")
        print(f"this server is {recieve_list[0]}")
        print(f"the number choosen by you is {num}")
        print(f"the number choosen by the server is {recieve_list[1]}")
        print(f"their sum is {num + int(recieve_list[1])}")
        client_socket.close()
        break



