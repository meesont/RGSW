#Password generator
from random import choice as r

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-"


passwords = []
password = ''
#passFor = input("Enter the website you'd like to create a password for: ")
passAmount = int(input("Enter the number of passwords you'd like: "))
amount = int(input("Enter the amount of characters you'd like: "))
for i in range (passAmount):
    for c in range (amount):
        password += r(chars)
    passwords.append(password)
    password = ''   
for i in range(len(passwords)):
    print(passwords[i])