import string
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
