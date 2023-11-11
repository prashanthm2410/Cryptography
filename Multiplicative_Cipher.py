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

def multiplicativeinverse(b, a):
    for i in range (1,27):
        if (a * i) % 26 == 1:
            A = i
            break
    return A


def decryption():
    ct = input("Enter the Encrypted message >> ")
    k = int(input("Enter the key used for encryption >> "))
    key = int(multiplicativeinverse(26, k))
    if key < 0:
        key += 26
    if key == -1:
        print(f"ERROR : Concurrent key for {k} does not exist...")
        exit()
    pt = ""
    for i in ct:
        pos = 0
        pos = l.index(i)
        n = int(pos/key)
        n1 = n % 26
        pt += l[int(pos*key)%26]
    print(f"Original message is >> {pt}")
encryption()
decryption()
