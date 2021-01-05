from TweetUtil import TweetUtil

tweetUtil = TweetUtil()
tweet_id_list, tweet_text_list = tweetUtil.get_timeline()
print("ツイート数", len(tweet_id_list))
if len(tweet_id_list) == 0:
    print("ツイートはありません")
else:
    for i in range(len(tweet_id_list)):
        tweetUtil.excute_reply(tweet_text_list[i], tweet_id_list[i])
