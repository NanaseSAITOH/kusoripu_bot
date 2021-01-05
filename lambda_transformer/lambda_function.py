# coding: utf-8
import json
import os
import ctypes
from learnning_model.PredictTaskExecutor import PredictTaskExecutor


def lambda_handler(event, context):
    sentence = event['text']
    predictTaskExecutor = PredictTaskExecutor()
    decode_sentence = predictTaskExecutor.main(sentence)

    res_body = {'encode_sentence': sentence,'decode_sentence': decode_sentence}
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(res_body)
    }
