import string
from unicodedata import digit
import random

letterlow = list(string.ascii_lowercase)
letterupper= list (string.ascii_uppercase)
digi = list(string.digits)

passlength=("enter password length: ")

while True:
    try:
        passlength = int(passlength)
        if passlength<8:
            print("you need at least 8 ")
            passlength= input("Please enter the number again: ")
        else:
            break
    except:
        print("please enter number only ")
        passlength= input("enter password length: ")

random.shuffle(letterlow)
random.shuffle(letterupper)
random.shuffle(digi)

numofletterlow= round(passlength * 30/100)
numofletterupper = round (passlength * 40/100)
numofdigit= round (passlength * 30/100)


password= []

for x in range(numofletterlow):
    password.append(letterlow[x])

for x in range(numofletterupper):
    password.append(letterupper[x])

for x in range(numofdigit):
    password.append(digi[x])

random.shuffle(password)

password="".join(password[0:])
print(f'Your password is: {password}')

