import json
from var import my_id
from client import encrypt_send
from msg import find_ip

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
    for x in cast_calc(msg[1]):
                print(f"sent to {x}")
                #send(find_ip(x), )