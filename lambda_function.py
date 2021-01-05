# coding: utf-8
import json
import os
import ctypes
from learnning_model.PredictTaskExecutor import PredictTaskExecutor

import MeCab

tagger = MeCab.Tagger(
    '-O wakati -r /dev/null -d /mnt/lambda/lib/mecab/dic/ipadic')

def lambda_handler(event, context):
    req_body = json.loads(event['body'])
    sentence = req_body['text']

    predictTaskExecutor = PredictTaskExecutor()
    decode_sentence = predictTaskExecutor.main(sentence)

    res_body = {
        'encode_sentence': sentence,'decode_sentence': decode_sentence
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(res_body)
    }
