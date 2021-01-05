# coding: utf-8
import json
from TweetUtil import TweetUtil

def lambda_handler(event, context):
    tweetUtil = TweetUtil()
    tweet_id_list, tweet_text_list = tweetUtil.get_timeline()
    if len(tweet_id_list) != 0:
        for i in range(len(tweet_id_list)):
            tweetUtil.excute_reply(tweet_text_list[i], tweet_id_list[i])
    # TODO implement
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }