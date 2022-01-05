from var import my_id
from client import send,find_ip
import json
import time

def cast(msg):
    def cast_calc(cast_id):
        cast_id = cast_id
        if cast_id[0] == "all":
            cast_id = list(json.loads(open("data/ip.json", "r").read()).keys())
        if cast_id.index(my_id) + 2 == len(cast_id):
            send = [int(((cast_id.index(my_id) + 1) + 1) / 2), len(cast_id)]
        else:
            send = [int(((cast_id.index(my_id) + 1) + 1) / 2), int((len(cast_id) + cast_id.index(my_id) + 1) / 2)]
        for x in send:
            send[send.index(x)] = cast_id[x-1]
        return(send)
    orig_msg = msg
    msg = eval(msg)[0]
    msg_hash = hash(str(msg))
    hash_file = open("data/cast_message", "r")
    hash_list = eval(hash_file.read())
    hash_file.close()
    if msg_hash in hash_list:
        return(0)
    else:
        hash_list.append(msg_hash)
        hash_file = open("data/cast_message", "w")
        hash_file.write(str(hash_list))
        hash_file.close()
        for x in cast_calc(msg[2][1]):
                    send(0, f'["ID", "{x}"]', str(orig_msg))
        return(1)

def msg_process(ip, msg):
    try:
        orig_msg = msg
        msg = eval(msg)[0]
        result = None
        while True:
            time = msg[0]
            id = msg[1]
            action = msg[2]
            if action[0] == '!HELLO!':
                print(f"hello form {id} at {time}")
                result = ['!message_recived!']
            elif action[0] == '?IP?':
                print(f"asking {action[1]}'s ip form {id} at {time}")
                result = ['!IP!', f"{find_ip(action[1])}"]
            elif action[0] == '!CAST!':
                if cast(orig_msg) == 1: #first time
                    msg = action[2]
                else:
                    result = ['!message_recived!']
            else:
                result = ['!message_not_recognized!']
            while result:
                return(result)
    except:
        return(['!error!'])