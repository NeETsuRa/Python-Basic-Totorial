import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'

port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pythonprogramming.net", 80))

s.send(request.encode())
result = s.recv(4096)

#print(result)
while (len(result) > 0):
    print(result)
    result = s.recv(4096)

#target = input('What website to scan?: ')
target = 'https://www.hackthissite.org/'
def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(25):
    if pscan(x):
        print('Port',x,'is open')	

exec("def test(): print('oooo snap!!!')")
test()