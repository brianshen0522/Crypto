import threading
import os
import json
import time
from rsa import sign
from server import server_start
from client import send
from var import my_id

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

if os.sys.argv[1] == "server":
    server = threading.Thread(target = server_start())
    server.start()
else:
    while True:
        participate = input("who do you want to send it to?")
        action = input("what do you want to do?")
        if action == "hello":
            msg = ['!HELLO!']
        elif action == "ip":
            ask_ip = input("who's ip?")
            msg = ['?IP?', f'{ask_ip}']
        elif action == "msg":
            msg = f"[{input('msg:')}]"
        print(send(1, f'["ID", "{my_id}"]', eval(f"['{int(time.time())}','{my_id}', ['!CAST!', {participate.split(' ')}, ['{int(time.time())}','{my_id}', {msg}]]]")))