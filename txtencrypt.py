i = 0
import random
def encrypt(key, input):
    f = open(input, 'r')
    output = ""
    random.seed(key)
    for char in f.read():
        m = chr(ord(char) + random.randrange(1, 26))
        output = output + m
        print(ord(m))
    b = open("encrypted file","w")
    b.write(output)
    b.close
    return(output)
def decrypt(key, input):
    f = open(input, 'r')
    output = ""
    random.seed(key)
    for char in f.read():
        m = chr(ord(char) - random.randrange(1, 26))
        output = output + m
        print(ord(m))
    b = open("decrypted file","w")
    b.write(output)
    b.close
    return(output)

while i == 0:
    print("encrypt or decrypt?")
    z = input()
    if z == "encrypt":
        print("input key")
        x = input()
        print("input file name")
        y = input()
        print(encrypt(x, y))
    else:
        if z == "decrypt":
            print("input key")
            x = input()
            print("input file name")
            y = input()
            print(decrypt(x, y))
