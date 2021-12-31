#from msg import msg_process
from rsa import sign, verify
import socket
import json
import threading

HEADER = 64
PORT = 1111
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT!"

def encrypt_send(IP, msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # define connection type
    client.connect((IP,  PORT)) #connect
    message = sign(msg).encode(FORMAT) #set message
    msg_length = len(message) #message len
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #send message len
    client.send(message) #send message
    while True:
        rec_msg = client.recv(2048).decode(FORMAT) #rec_msg = recive message
        if rec_msg:
            if verify(rec_msg):
                msg = eval(rec_msg)[0]
                print(msg)
                break;
            else:
                print("message has been distort")
                break
    msg_length = len(DISCONNECT_MESSAGE) #set disconnect message len
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #send disconnect message len
    client.send(DISCONNECT_MESSAGE.encode(FORMAT)) #send dissconnect message
    return (rec_msg);

def send(IP, msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # define connection type
    client.connect((IP,  PORT)) #connect
    message = msg.encode(FORMAT) #set message
    msg_length = len(message) #message len
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #send message len
    client.send(message) #send message
    while True:
        rec_msg = client.recv(2048).decode(FORMAT) #rec_msg = recive message
        if rec_msg:
            if verify(rec_msg):
                msg = eval(rec_msg)[0]
                print(msg)
                break;
            else:
                print("message has been distort")
                break
    msg_length = len(DISCONNECT_MESSAGE) #set disconnect message len
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #send disconnect message len
    client.send(DISCONNECT_MESSAGE.encode(FORMAT)) #send dissconnect message
    return (rec_msg);