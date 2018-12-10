# # @Author: Thomas Meeson <Thomas>
# # @Date:   10-12-2018
# @Last modified by:   thomas
# @Last modified time: 10-12-2018
# # @License: Licensed under the Apache License, Version 2.0 (the "License");
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
# # @Copyright: Copyright 2018 Thomas Meeson

import requests as r

response = r.get('https://www.hipstercode.com/')

# linksList = [
# 'https://schoolweb.rgsw.org.uk/'
# ]
# response.encoding = 'ISO-8859-1'

class LoginPage:
    def __init__(self, siteLink, username, passworrd, token):
        self.password = password
        self.siteLink = siteLink
        self.username = username
        self.token = token


loginPage = 'https://schoolweb.rgsw.org.uk/Login/login.aspx?prelogin=https%3a%2f%2fschoolweb.rgsw.org.uk%2f'
loginName = 'username'
passwordName = 'password'

outfile = '/Users/thomas/Documents/School Coding - Github/RGSW/Python/scrapingOutfile.txt'

with open(outfile, 'w') as f:
    f.write(str(response.text))
