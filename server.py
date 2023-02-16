import socket
import random
import threading
import time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address="127.0.0.1"
port=8000

server.bind((ip_address,port))
server.listen()

clients=[]
nicknames=[]

print("[STARTED] server started successfully...")


questions={
    "Who developed Python Programming Language?\na) Wick van Rossum\nb) Rasmus Lerdorf\nc) Guido van Rossum\nd) Niene Stom":"c",
    "Which type of Programming does Python support?\na) object-oriented programming\nb) structured programming\nc) functional programming\nd) all of the mentioned":"d",
}

def get_random_question(conn,nickname):

    # generating a random question and sending it
    list_of_questions=list(questions.keys())
    random_index=random.randint(0,len(questions)-1)
    random_question=list_of_questions[random_index]
    conn.send(random_question.encode("utf-8"))

    # storing the players answer
    player_answer=conn.recv(2048).decode("utf-8")

    # evaluating the answer
    if player_answer==questions[random_question]:
        conn.send(f"{player_answer} Correct answer".encode("utf-8"))
    else:
        conn.send(f"{player_answer} wrong answer".encode("utf-8"))
        conn.send(random_question.encode("utf-8"))

def client_thread(conn,nickname):
    player_score=0
    intro="Welcome to this quiz game!\nyou will receive a question. The answer to that question should be one of a ,b ,c ,d\nGood Luck..!"
    conn.send(intro.encode("utf-8"))
    time.sleep(1)
    get_random_question(conn,nickname)
    


while True:
    conn,addr=server.accept()
    clients.append(addr[0])
    conn.send("nickname".encode("utf-8"))
    nickname=conn.recv(2048).decode("utf-8")
    nicknames.append(nickname)

    print(f"{nickname} joined")

    threading.Thread(target=client_thread,args=(conn,nickname)).start()