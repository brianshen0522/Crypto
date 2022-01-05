#from msg import msg_process
from rsa import sign, verify
import socket
import json
import threading

HEADER = 64
PORT = 1111
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT!"

def find_ip(id):
    ip_file = open("data/ip.json", "r")
    ip_list = json.loads(ip_file.read())
    return(ip_list[id])

def connection_failed (id):
    pass

def send(encrypt, ID_IP, msg):
    ID_IP = eval(ID_IP)
    if ID_IP[0] == "ID":
        IP = find_ip(ID_IP[1])
    elif ID_IP[0] == "IP":
        IP = ID_IP[1]
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # define connection type
        client.connect((IP,  PORT)) #connect
        if encrypt == 1:
            message = str(sign(msg)).encode(FORMAT) #set message
        elif encrypt == 0:
            message = str(msg).encode(FORMAT) #set message
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
                    rec_msg = msg
                    break;
                else:
                    print("message has been distort")
                    break
        msg_length = len(DISCONNECT_MESSAGE) #set disconnect message len
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length) #send disconnect message len
        client.send(DISCONNECT_MESSAGE.encode(FORMAT)) #send dissconnect message
        return(rec_msg);
    except:
        connection_failed(IP)
        pass