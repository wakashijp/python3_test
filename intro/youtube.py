# coding=utf-8

# intro/youtube.py
# 入門 Python 3
# 2015-12-06

# 例 1-1 intro/youtube.py
import json
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])

#  8行目：jsonというPython標準ライブラリから全てのコードをインポートする。
#  9行目：urllibという標準ライブラリからurlopen関数だけをインポートする。
# 10行目：url変数にYouTubeのURLを代入する。*1
# 11行目：指定されたURLのウェブサーバーに接続し、特定のウェブサービスを要求する。
# 12行目：応答データを受け取り、contents変数に代入する。
# 13行目：contentsをJSON形式の文字列にデコードし、結果をtext変数に代入する。
# 14行目：textをdata、すなわちPythonのデータ構造に変換する。
# 15行目：動画についての情報を一度にひとつずつvideo変数に取り出す。
# 15行目：2レベルのPython辞書（data['feed']['entry']）とスライス（[0:6]）を使って情報を切り出す。
# 15行目：print関数を使って動画のタイトルだけを表示する。
# *1 監訳注：原書のコードではYouTubeの古いAPI(https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json)
# が使われており、そのAPIは既に廃止されているため動作しない。そのため日本語翻訳版の本書では、固定された結果を返すAPI
# (https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json)
# を別途用意し利用している。
