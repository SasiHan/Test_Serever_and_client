import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.1.162'
port = 5000
try:
    s.connect((host,port))
    msg = input ("Please Report Your Paid! : ")
    Total = f"Amount of value {msg}!!"

    s.send(Total.encode(encoding='UTF-8',errors='strict'))
    data = s.recv(1024)
    print (data.decode(encoding='UTF-8',errors='strict'))
    s.close()
except socket.error as Total:
    print('Bind failed. Error Code :'+str(msg[0])+'Message'+msg[1])