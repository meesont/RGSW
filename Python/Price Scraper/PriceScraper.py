# @Author: Thomas Meeson <thomas>
# @Date:   03-07-2019
# @Last modified by:   thomas
# @Last modified time: 03-07-2019
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

import requests as r
from bs4 import BeautifulSoup
import smtplib
import sys
import time

VERSION = '1.0-RELEASE'

def findPrice(url, password, priceToDropToo):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    page = r.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    itemTitle = soup.find(id='productTitle').get_text().strip()
    itemPrice = soup.find(id='priceblock_ourprice').get_text()

    itemPrice = float(itemPrice[1:])

    if(itemPrice < float(priceToDropToo)):
        print('Price fall detected')
        print(f'Price is {itemPrice}')
        sendMail(website, password)
    else:
        print("No price fall detected")
    # print(itemTitle)
    # print(itemPrice)


def sendMail(website, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('meesondev@gmail.com', password)

    subject = "Price Fall"
    body = "Link to updated price:\n"

    msg = f'Subject: {subject} \n\n{body}{website}'

    server.sendmail(
        'meesondev@gmail.com',
        'thomas.meeson@gmail.com',
        msg
    )

    print('Price drop detected, email sent!')

    server.quit()


if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print(f"\nWelcome to PriceScraper v{VERSION}")
        print("Continuely checks the price of an amazon link for any price drop, then emails user")
        print('\nUsage: python3 PriceScraper.py <pass> <priceDrop> <cycleTime>\n')
    else:
        password = sys.argv[1]
        priceDrop = sys.argv[2]
        cycleTime = sys.argv[3]
        print(f"\nWelcome to PriceScraper v{VERSION}\n")
        print(f"\nCycling every {cycleTime} minutes ({float(cycleTime) * 60} seconds)")
        print(f'Detecting prices below £{float(priceDrop)}')
        website = 'https://www.amazon.co.uk/Amazon-Echo-Dot-Smart-Speaker-Alexa/dp/B0792KWK57/ref=sr_1_1?keywords=alexa&qid=1562158415&s=electronics&sr=1-1'
        while(True):
            findPrice(website, password, priceDrop)
            time.sleep(float(cycleTime) * 60)  # Run every cycleTime limitations
