import threading
import os
import json
import time
from msg import find_ip
from server import server_start
from client import encrypt_send
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
        id = input("who do you want to send it to?")
        action = input("what do you want to do?")
        if action == "hello":
            encrypt_send(find_ip(id), f"['{int(time.time())}','{my_id}', ['!HELLO!']]")
        elif action == "ip":
            ask_ip = input("who's ip?")
            encrypt_send(find_ip(id), f"['{int(time.time())}','{my_id}', ['?IP?', '{ask_ip}']]")
        elif action == "cast":
            participate = input("who do you want to send it to?")
            msg_to_cast = input("what message do you wnat to send?")
            encrypt_send(find_ip(id), f"['{int(time.time())}','{my_id}', ['!CAST!', {participate.split(' ')}, '{msg_to_cast}']]")
        else:
            msg = input('msg?')
            encrypt_send(find_ip(id), f"['{int(time.time())}','{my_id}', '{msg}']")