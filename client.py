import socket
import threading
import random

nickname=input("Enter you name to join : ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000

client.connect((ip_address,port))
print("Connected..")

def recv():
    while True:
        try:
            msg=client.recv(2048).decode("utf-8")
            if msg=="nickname":
                client.send(nickname.encode("utf-8"))
            else:
                print(msg)
        except:
            print("an error occured!")
            client.close()

def write():
    while True:
        msg=f'{nickname}: {input("")}'
        client.send(msg.encode("utf-8"))



recv_thread=threading.Thread(target=recv)
recv_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()