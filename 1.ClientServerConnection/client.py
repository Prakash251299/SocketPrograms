import socket
HOST = '127.0.0.1'
PORT = 5555
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)
while True:
    mes = input(">")
    client_socket.send(mes.encode())
    res = client_socket.recv(1024).decode()
    print(res)
    if mes == "exit":
        break
client_socket.close()


# # Import socket module
# import socket			

# # Create a socket object
# s = socket.socket()		

# # Define the port on which you want to connect
# port = 5555		

# # connect to the server on local computer
# s.connect(('127.0.0.1', port))
# while True:
#     a = input("Enter 'a' to continue")


#     # receive data from the server and decoding to get the string.
#     print(s.recv(1024).decode())
#     # close the connection
#     # s.close()	
	
