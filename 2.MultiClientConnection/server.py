import socket
import threading
host = '127.0.0.1'
port = 5555
s = socket.socket()
s.bind(('',port))
s.listen(5)
print("socket is listening")
clients = []
def handle_client(conn,addr):
    while True:
        # conn,addr = s.accept()
        conn.send("Thank you for connecting".encode())
        # print("hi")


        clients.append(conn)
        mes = conn.recv(1024).decode()
        print(f"{port}: {mes}")
        if(mes == "exit"):
            break
        else:
            for c in clients:
                if c!=conn:
                    conn.send(f"{addr}: {mes}\n".encode())
    clients.remove(conn)

    conn.close()
    print(f"Disconnected")
while True: 
    client_socket, client_address = s.accept()
    print(f"Connected to {client_address}...")
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address)) 
    client_thread.start()
