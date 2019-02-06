# @Author: Thomas Meeson <meesont>
# @Date:   26-10-2018
# @Last modified by:   thomas
# @Last modified time: 06-02-2019
# @License: Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Copyright: Copyright © 2018 Thomas Meeson


#Password generator
import random as r

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-[]{};/`=+_"
#Creating more secure passwords

password = ''
passChars = int(input("Input the number of chars for the password: "))
passLevel = input("Enter Password Secruity Level (Strong/Normal/Weak): ").lower()
passFile = input("Enter the name of the file to store these passwords in (Exclude extention): ")
# passFile = "passwords"

def createPassword(num):
    for i in range(num):
        pw += r(chars)

if(passLevel == 'strong'):
    password = 'hello1'
elif(passLevel == 'normal'):
    password = 'hello2'
elif (passLevel == 'weak'):



print(password)

# passwords = []
# password = ''
# #passFor = input("Enter the website you'd like to create a password for: ")
# passAmount = int(input("Enter the number of passwords you'd like: "))
# amount = int(input("Enter the amount of characters you'd like: "))
# for i in range (passAmount):
#     for c in range (amount):
#         password += r(chars)
#     passwords.append(password)
#     password = ''
# for i in range(len(passwords)):
#     print(passwords[i])


# for i in range(passChars):
#     password += r.choice(chars)
# file = open('.'.join([passFile, "txt"]), 'w')
# file.write(password)
# file.close()
# print(password)
