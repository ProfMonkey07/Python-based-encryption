i = 0
import random
def encrypt(key, input):
    f = open(input, 'r')
    output = ""
    random.seed(key)
    for char in f.read():
        #generates new unicode value for that character
        m = chr(ord(char) + random.randrange(-10, 10))
        output = output + m
        print(m)
        print(ord(m))
    b = open(str(input.split('.')[0] + "(enc)" + input.split('.')[1]),"w")
    b.write(output)
    b.close
    return(output)
def decrypt(key, input):
    f = open(input, 'r')
    output = ""
    random.seed(key)
    for char in f.read():
        #reverts unicode value for that character back to what it was before encryption
        m = chr(ord(char) - random.randrange(-10, 10))
        output = output + m
        print(m)
        print(ord(m))
    b = openstr(input.split('.')[0] + "(dec)" + input.split('.')[1]),"w")
    b.write(output)
    b.close
    return(output)

while i == 0:
    #what you see on the console and how to interact with the program
    print("encrypt or decrypt?")
    z = input()
    if z == "encrypt":
        print("input key")
        x = input()
        print("input file name")
        y = input()
        print(str(encrypt(x, y)))
    else:
        if z == "decrypt":
            print("input key")
            x = input()
            print("input file name")
            y = input()
            print(str(decrypt(x, y)))
