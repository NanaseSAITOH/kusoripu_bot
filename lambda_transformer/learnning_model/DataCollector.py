import random
import numpy as numpy

import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
import torch.nn.functional as F

import pickle


class DataCollector:

    def load_data():
        # 単語ファイルロード
        with open('/mnt/lambda/Data/words.pickle', 'rb') as ff:
            words = pickle.load(ff)

        with open('/mnt/lambda/Data/maxlen.pickle', 'rb') as maxlen:
            [maxlen_e, maxlen_d] = pickle.load(maxlen)

        with open('/mnt/lambda/Data/indices_word.pickle', 'rb') as i2w:
            indices2word = pickle.load(i2w)

        with open('/mnt/lambda/Data/word_indices.pickle', 'rb') as w2i:
            word2indices = pickle.load(w2i)

        print(word2indices["　"])

        data = {
            'maxlen_e': maxlen_e,
            'maxlen_d': maxlen_d,
            'indices2word': indices2word,
            'word2indices': word2indices,
            'input_dim': len(words),
            'output_dim': len(words),
            'words': words
        }
        return data
