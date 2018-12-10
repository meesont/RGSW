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


#Intermediate Python stuff
from os import path

names = ["Tom","Jon","Bob","Chris"]

for name in names:
    output = ' '.join(["hello there,", name])
    print (output)


filePath = "/Users/thomas/Documents/School Coding - Github/RGSW/Python/Intermediate Python Stuff"
fileName = "default.txt"

#Use .join rather than using +
#.join scales better than + does therefore better for larger projects

with open(path.join(filePath, fileName)) as file:
    print(file.read())


name = "Tim"
apples = 10

print(f"Today {name} bought {apples} apples!")
print("Today {} bought {} apples!".format(name, apples))
