import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.162'
port = 5000
try:
    s.bind((host, port))
    print("Socket Binded to %s" % port)
except socket.error as msg:
    print('Bind failed. Error Code :' + str(msg[0]) + ' Message ' + msg[1])
    exit()

s.listen(5)
print("Socket is listening")
while True:
    conn, address = s.accept()
    print("Connected to: ", address)

    data = conn.recv(1024)
    print('Data :', data.decode(encoding='UTF-8', errors='strict'))
    if not data:
        msg = "Sorry it's Not Data!"
        break
    msg = 'Thank you for reporting'

    conn.send(msg.encode(encoding='UTF-8', errors='strict'))

conn.close()
s.close()