import json #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = "vPVdfstGdvW3uEc4CALVeTvjf"                          # Consumer Key
CS = "ZVSff6RDG3l5LcG6NWvyKZgn8MVD01rwZZ0MPTwC4hplSzpl0r"    # Consumer Secret
AT = "3282531025-TjQaPI1FanOFHPeGIE1ZnMczZQ08RJ1ezJJ8Atl"    # Access Token
ATS = "f03WejeQ6aRiULyrCpU8znYbHk0fdjSE7RoB4860LgFmX"

twitter = OAuth1Session(CK, CS, AT, ATS)  #認証処理

tweet_id = 0
tweet_text = ""
kusorep_id = 0
kusorep_text = ""

url = "https://api.twitter.com/1.1/search/tweets.json"  #タイムライン取得エンドポイント
url2 = "https://api.twitter.com/1.1/statuses/show.json"  #タイムライン取得エンドポイント

params = {'q': 'クソリプ乙', 'count' : 1} #取得数
res = twitter.get(url, params = params)

if res.status_code == 200: 
    timelines = res.json()['statuses']  
    for line in timelines:  
        print("クソリプ乙:", line['text'])
        kusorep_id = line['in_reply_to_status_id']
else: 
    print("Failed: %d" % res.status_code)

kusorep_param = {'id': kusorep_id} #取得数
kusorep_res = twitter.get(url2, params=kusorep_param)

if kusorep_res.status_code == 200: #正常通信出来た場合
    timelines = kusorep_res.json()  #レスポンスからタイムラインリストを取得
    print("kusorep_text:", timelines['text'])
    kusorep_text = timelines['text']
    tweet_id = timelines['in_reply_to_status_id']
else: #正常通信出来なかった場合
    print("Failed: %d" % kusorep_res.status_code)

tweet_param = {'id': tweet_id} #取得数
tweet_res = twitter.get(url2, params=tweet_param)

if tweet_res.status_code == 200: #正常通信出来た場合
    timelines = tweet_res.json()  #レスポンスからタイムラインリストを取得
    #print(timelines)
    print("tweet_text:", timelines['text'])
    tweet_text = timelines['text']
else: #正常通信出来なかった場合
    print("Failed: %d" % tweet_res.status_code)
