import socket
host = '127.0.0.1'
port = 5555
s = socket.socket()
s.connect((host,port))
wlcm = s.recv(1024).decode()
print(wlcm)
while True:
    mes = input(">")
    s.send(mes.encode())
    res = s.recv(1024).decode()
    print(res)
    if mes == "exit":
        break
s.close()