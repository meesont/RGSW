# @Author: Thomas Meeson <thomas>
# @Date:   13-05-2019
# @Last modified by:   thomas
# @Last modified time: 13-05-2019
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
# @Copyright: Copyright(c) 2019 Thomas Meeson

import random as r

guessNum = r.randrange(1,20)

userInput = int(input('Enter a number between 1 and 20: '))

while (userInput != guessNum):
    if(userInput < guessNum):
        print('You guessed less than the guess number!')
        userInput = int(input('Enter another number between 1 and 20: '))
    elif(userInput > guessNum):
        print('You guessed more than the guess number!')
        userInput = int(input('Enter another number between 1 and 20: '))

print(f'You guessed correctly the number was: {guessNum}')
