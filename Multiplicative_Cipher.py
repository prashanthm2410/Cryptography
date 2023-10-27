import random
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption():
    pt = input("Enter the Original message >> ")
    key = int(input("Enter the key >> "))
    ct = ""
    for i in pt:
        pos= 0
        pos = l.index(i)
        ct += l[(pos*key)%26]
    print(f"Encrypted message is >> {ct}")

def extendedeuclid(key):
    r1 = 26
    r2 = key
    t1 = 0
    t2 = 1
    while r2 > 0:
        r = r1 % r2
        q = (r1-r)/r2
        r1 = r2
        r2 = r
        t = t1 * q - t2
        t1 = t2
        t2 = t
    return t1

def decryption():
    ct = input("Enter the Encrypted message >> ")
    key = extendedeuclid(int(input("Enter the key used for encryption >> ")))
    pt = ""
    for i in ct:
        pos = 0
        pos = l.index(i)
        pt += l[(pos*key)%26]
    print(f"Original message is >> {pt}")


encryption()
decryption()
