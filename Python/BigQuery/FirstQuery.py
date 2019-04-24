# @Author: Thomas Meeson <thomas>
# @Date:   16-04-2019
# @Last modified by:   thomas
# @Last modified time: 19-04-2019
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

from google.cloud import bigquery
# import os
client = bigquery.Client()


# query = (
#     "SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` "
#     'WHERE state = "TX" '
#     "LIMIT 100"
# )

query = (
    'SELECT tags, title, id FROM `bigquery-public-data.stackoverflow.stackoverflow_posts` '
    'WHERE tags LIKE "%java"'
    'LIMIT 10'
)

query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
)  # API request - starts the query

for row in query_job:  # API request - fetches results
    # Row values can be accessed by field name or index
    # assert row[0] == row.name == row["name"]
    print(row['title'])
    print(row['id'])
    print(row['tags'])
    # print('')
    # print('')
