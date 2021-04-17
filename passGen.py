import random
import string
def passwordgen(n):
    for i in range(n):
        print(random.choice(string.ascii_letters), end='')
    return
number=input("please enter numeric password length")
passwordgen(int(number))