# @Author: Thomas Meeson <Thomas>
# @Date:   10-12-2018
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
from bs4 import BeautifulSoup

response = r.get('https://schoolweb.rgsw.org.uk/')

soup = BeautifulSoup(response.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
# print(soup.prettify())


# print(response.text)

outfile = '/Users/thomas/Documents/School Coding - Github/RGSW/Python/scrapingOutfile.txt'


#
# schoolweb = (
# 'username': "username",
# 'password': "password",
# 'token': 'unknown',
# 'loginpage': 'https://schoolweb.rgsw.org.uk/Login/login.aspx?prelogin=https%3a%2f%2fschoolweb.rgsw.org.uk%2f'
#
# session = r.session()


# with open(outfile, 'w') as f:
#     f.write(str(response.text))
