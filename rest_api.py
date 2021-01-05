from flask import Flask, jsonify, request
from learnning_model.PredictTaskExecutor import PredictTaskExecutor
import json

app = Flask(__name__)


@app.route('/predict')
def hello():
    sentence = request.args.get('sentence')
    predictTaskExecutor = PredictTaskExecutor()
    decode_sentence = predictTaskExecutor.main(sentence)
    print(decode_sentence)

    return_json = json.dumps({'encode_sentence': sentence,
                              'decode_sentence': decode_sentence}, ensure_ascii=False)

    return return_json


if __name__ == '__main__':
    app.run(use_reloader=False, threaded=False)
