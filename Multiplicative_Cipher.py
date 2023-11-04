import random
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption():
    pt = input("Enter the Original message >> ")
    key = int(input("Enter the key >> "))
    ct = ""
    for i in pt:
        pos= 0
        pos = l.index(i)
        print(f"epos = {pos}")
        ct += l[(pos*key)%26]
    print(f"Encrypted message is >> {ct}")

def multiplicativeinverse(a, b):
    if a == 0:
        return b
    for i in range(1, b):
        if ((a % b) * (i % b)) % b == 1:
            return b
    return -1


def decryption():
    ct = input("Enter the Encrypted message >> ")
    k = intimport string
#string.ascii_lowercase
sm = list(string.ascii_lowercase)

def encryption():
    pt = input("Enter the original message >> ")
    a = int(input("Enter first key >> "))
    b = int(input("Enter second key >> "))
    x = 0
    ct = ""
    for i in pt:
        x = sm.index(i)
        ct += sm[(a * x + b) % 26]
    print(f"ct = {ct}")

encryption()
(input("Enter the key used for encryption >> "))
    key = int(multiplicativeinverse(26, k))
    if key < 0:
        key += 26
    print(f"key = {key}")
    if key == -1:
        print(f"ERROR : Concurrent key for {k} does not exist...")
        exit()
    pt = ""
    for i in ct:
        pos = 0
        print(f"i={i}")
        pos = l.index(i)
        print(f"pos = {pos}")
        n = int(pos/key)
        print(f"n = {n}")
        n1 = n % 26
        print(f"n1 = {n1}")
        pt += l[int(pos/key)%26]
        print(pt)
    print(f"Original message is >> {pt}")

encryption()
decryption()

