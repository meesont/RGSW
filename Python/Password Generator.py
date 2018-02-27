#Password generator
import random as r

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-"


passwords = []
password = ''
passAmount = int(input("Enter the number of passwords you'd like: "))
amount = int(input("Enter the amount of characters you'd like: "))
for i in range (passAmount):
    for c in range (amount):
        password += r.choice(chars)
    passwords.append(password)
    password = ''   
for i in range(len(passwords)):
    print(passwords[i])