from var import my_id
from client import send,encrypt_send
import json

def find_ip(id):
    ip_file = open("data/ip.json", "r")
    ip_list = json.loads(ip_file.read())
    return(ip_list[id])

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

def cast(msg):
    orig_msg = msg
    msg = eval(eval(msg)[0])
    msg_hash = hash(str(msg))
    hash_file = open("data/cast_message", "r")
    hash_list = eval(hash_file.read())
    hash_file.close()
    if msg_hash in hash_list:
        print("repeat")
        pass
    else:
        hash_list.append(msg_hash)
        hash_file = open("data/cast_message", "w")
        hash_file.write(str(hash_list))
        hash_file.close()
        for x in cast_calc(msg[2][1]):
                    print(f"sent to {x}")
                    #print(orig_msg)
                    send(find_ip(x), str(orig_msg))

def msg_process(msg):
    orig_msg = msg
    msg = eval(eval(msg)[0])
    time = msg[0]
    id = msg[1]
    action = msg[2]
    if action[0] == '!HELLO!':
        print(f"hello form {id} at {time}")
        result = ['!message_recived!']
    elif action[0] == '?IP?':
        print(f"asking {action[1]}'s ip form {id} at {time}")
        result = ['!IP!', f"{find_ip(action[1])}"]
    elif action[0] == '!IP!':
        print(action[1])
    elif action[0] == '!CAST!':
        print(f"cast {action[2]} to {action[1]} form {id} at {time}")
        cast(orig_msg)
        result = ['!message_recived!']
    else:
        result = ['!message_not_recognized!']
    if result:
        return(result)
    else:
        return