from os import close

f = open("public.pem", "r")
key = f.read()[27:-25].replace("\n", " ")
f.close
f = open("public.pem", "w")
f.write(key)
f.close

# f = open("public.pem", "r")
# key = open("public.pem", "r").read()
key = "-----BEGIN PUBLIC KEY-----"+"\n"+open("public.pem").read().replace(" ", "\n")+"\n"+"-----END PUBLIC KEY-----"
print(open("public.pem").read())