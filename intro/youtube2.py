# coding=utf-8

# intro/youtube2.py
# 入門 Python 3
# 2015-12-09

# 例 1-2 intro/youtube2.py
import requests
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
