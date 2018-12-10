# @Author: Thomas Meeson <meesont>
# @Date:   26-10-2018
# @Last modified by:   meesont
# @Last modified time: 26-10-2018
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

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-"


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


#Creating more secure passwords

password = ""
passChars = int(input("Input the number of chars for the password: "))
# passLevel = input("Enter Password Secruity Level (Strong/Average): ")
passFile = input("Enter the name of the file to store these passwords in (Exclude extention): ")
passFile = "passwords"
#
#
# if (passLevel == ("strong" or "Strong" or "STRONG")):
#     # TODO: strong code
#
# else:

for i in range(passChars):
    password += r.choice(chars)
file = open('.'.join([passFile, "txt"]), 'w')
file.write(password)
file.close()
print(password)
