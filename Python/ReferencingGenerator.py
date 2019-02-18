# @Author: Thomas Meeson <thomas>
# @Date:   18-02-2019
# @Last modified by:   thomas
# @Last modified time: 18-02-2019
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
# @Copyright: Copyright 2018 Thomas Meeson


import requests as r
from bs4 import BeautifulSoup as bs
import datetime as dt


#This is specific to stackoverflow as it finds specific classes which are used on stackoverflow to define titles ect


# link = 'https://stackoverflow.com/questions/9346954/doctype-html-what-does-it-mean'

def loadFile(fileName):
    links = []
    with open(fileName + '.txt', 'r') as f:
        links = f.readlines()
    return links

def createRef(link):
    response = r.get(link)

    soup = bs(response.content, 'html.parser')
    title = soup.find('div', id='question-header').find('a', class_='question-hyperlink').get_text() #This gets the title

    creationTime = soup.find('div', class_='user-action-time').find('span').get('title').split(' ')
    creationTime = creationTime[0].split('-')
    creationDate = creationTime[0]

    now = dt.datetime.now()
    # print(creationDate)

    outString = f"Stackoverflow ({creationDate}) '{title}' [online] {link} accessed {now.day}/{now.month}/{now.year}"
    return outString

if __name__ == '__main__':
    # links = loadFile('linkInputs')
    # refs = []
    # outfile = 'refGenerator'
    # for link in links:
    #     ref = createRef(link)
    #     refs.append(ref)
    #
    # with open(outfile + '.txt', 'w') as f:
    #     for i in refs:
    #         f.write(f + '\n')

    link = 'https://stackoverflow.com/questions/9346954/doctype-html-what-does-it-mean'

    print(createRef(link))

    # print(f'Completed writing {len(refs)} refs to file {outFile}.txt')
