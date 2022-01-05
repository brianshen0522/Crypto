from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.Hash import SHA
import base64
import os
import json

def create ():
    random_generator = Random.new().read
    print("creating key pair")
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()
    with open("keys/private.pem", "wb") as f:
        f.write(private_pem)
        print("private key......done")
    public_pem = rsa.publickey().exportKey()
    public_pem = public_pem.decode()
    f = open("keys/public.pem", "w")
    f.write(public_pem)
    f.close
    print("public key......done")
    print(public_pem[27:-25].replace("\n", " "))
    print("done")

def sign(message):
    rsakey = RSA.importKey(open("keys/private.pem").read())
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(str(message).encode("utf-8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    message = [message, eval(f"['{signature.decode('utf-8')}']")]
    return(message)

def verify(input_data):
    message = str(eval(input_data)[0])
    signature = eval(input_data)[1][0]
    pub = "-----BEGIN PUBLIC KEY-----"+"\n"+json.loads(open("keys/keys.json", "r").read())[f'{eval(message)[1]}'].replace(" ", "\n")+"\n"+"-----END PUBLIC KEY-----"
    rsakey = RSA.importKey(pub)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    hsmsg = SHA.new()
    hsmsg.update(message.encode("utf-8"))
    is_verify = verifier.verify(hsmsg, base64.b64decode(signature))
    if is_verify == True:
        return("verified")
    else:
        return("doctored")