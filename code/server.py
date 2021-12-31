from var import my_id
from rsa import verify, sign
from msg import msg_process
import socket
import threading
import time
import os
HEADER = 64 #set header length
PORT = 1111 #set server listening port
ADDR = ("0.0.0.0", PORT)
FORMAT = 'utf-8' #set format
DISCONNECT_MESSAGE = "!DISCONNECT!" #set disconnect message

def handle_connection(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)       #print(f"msg length:{msg_length}")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            #print(f"raw msg:{msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
                #print("connection end")
            else:#msg
                if verify(msg) == "verified":#if message is verified
                    reply = msg_process(msg)
                    conn.send(sign(f"[{int(time.time())},'{my_id}' ,{reply}]").encode(FORMAT))
                else:#if message is doctored
                    conn.send(DISCONNECT_MESSAGE.encode(FORMAT))
    conn.close()

def server_start():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #set connection type
        try:
            print("[STARTING] server is starting...")
            server.bind(ADDR) #start server
            server.listen() #listening
            print(f"[LISTENING] Server is listening on port {PORT}")
            while True:
                conn, addr = server.accept() #accept connection
                handle_msg = threading.Thread(target=handle_connection, args=(conn, addr)) #set a threat(handle_connection)
                handle_msg.start() #start thread(handle_connection)
        except:
            out = os.popen("sudo netstat -ltpn |grep 1111").read()
            out = out[80:out.find("/")]
            if out:
                os.system(f"sudo kill -9 {out}")