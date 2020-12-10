import socket

port = 8080
s = socket.socket()
host = ''

s.bind((host, port))
s.listen(5)

print('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='5.4.1.py'
    f = open(filename,'r')
    l = f.read(1024)
    while (l):
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()

