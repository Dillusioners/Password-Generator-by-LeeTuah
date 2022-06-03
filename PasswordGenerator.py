import random
from random import shuffle

kwc = int(input("Enter your keyword count: "))
kwlist = []
spchar = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', '+'])
spchar2 = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', '+'])
num = random.randint(0, 999999)
snum = str(num)
num2 = random.randint(1, 9999)
snum2 = str(num2)
passs = ""

if kwc >= 0:
    while kwc != 0:
        kw = input("Enter a unique keyword: ")
        kwlist.append(kw)
        kwc -= 1
    shuffle(kwlist)
    kbstick = len(kwlist) - 1
    while kbstick >= 0:
        kwlist[kbstick] = str.upper(kwlist[kbstick])
        kbstick = kbstick - 2
    kwlist.extend(spchar)
    kwlist.append(snum)
    kwlist.extend(spchar2)
    kwlist.append(snum2)
    for i in range(0, len(kwlist)):
        passs = passs + kwlist[i]
    print("Your Freshly generated password: ", passs)
else:
    print("Invalid Keyword, Try again")