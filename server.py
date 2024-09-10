#encoding:utf-8
import socket

host = '2001:861:5820:47f0:7d04:730f:3045:356e'
port = 11150

socket = socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur est démarré...")

while True:
    socket.listen()
    conn, adress = socket.accept()
    print("En écoute...")


conn.close()
socket.close()