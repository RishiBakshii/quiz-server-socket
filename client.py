import socket
import threading
import time


def loading_animation():
    animation = "|/-\\"
    idx = 0
    while idx<=20:
        print("Connecting with the server...",animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)

nickname=input("Enter your name to join the quiz : ")
time.sleep(1)
loading_animation()
time.sleep(2)



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
        time.sleep(10)
        msg=input("\nEnter your answer: \n\n")
        client.send(msg.encode("utf-8"))



recv_thread=threading.Thread(target=recv)
recv_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()