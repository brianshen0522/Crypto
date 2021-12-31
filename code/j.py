from var import my_id
import json

def cast(cast_id):
    if cast_id[0] == "all":
        cast_id = list(json.loads(open("data/ip.json", "r").read()).keys())
    print(cast_id.index(my_id))
    print(cast_id)
    if cast_id.index(my_id) + 2 == len(cast_id):
        send = [int(((cast_id.index(my_id) + 1) + 1) / 2), len(cast_id)]
    else:
        send = [int(((cast_id.index(my_id) + 1) + 1) / 2), int((len(cast_id) + cast_id.index(my_id) + 1) / 2)]
    for x in send:
        send[send.index(x)] = cast_id[x-1]
    return(send)

# cast_id = ["001", "002", "999"]
# print(cast(cast_id))

# hash_file = open("data/cast_message.json", "r+")
# file = hash_file.read()
# print(file)
# hash_list = json.loads(file)['message_hash']
# for x in hash_list:
#     print(x)
# hash_list = json.dumps(hash_list)
# print(hash_list, type(hash_list))
#hash_file.write(file)

hash_file = open("data/cast_message", "r+")
hash_list = eval(hash_file.read())
hash_list.append("hi")
print(hash_list, type(hash_list))