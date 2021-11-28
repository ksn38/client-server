'''#!/usr/bin/env python3
import urllib.request

fp = urllib.request.urlopen("csd_server_1.csd_csd")
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")
print(decodedContent)
fp.close()'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('csd_server_1', 1234))
string = 'hello, world!'
bytes = string.encode('utf-8')
sock.send(bytes)
data_bytes = sock.recv(1024)
sock.close()

print(data_bytes.decode('utf-8'))