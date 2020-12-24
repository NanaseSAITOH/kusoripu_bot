from sklearn.utils import shuffle
import random
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
import torch.nn.functional as F

import pickle


class DataCollector:
    def load_data():
        # 単語ファイルロード
        with open('words.pickle', 'rb') as ff:
            words = pickle.load(ff)

        with open('e.pickle', 'rb') as f:
            encoder = pickle.load(f)

        with open('d.pickle', 'rb') as g:
            decoder = pickle.load(g)

        with open('t.pickle', 'rb') as h:
            label = pickle.load(h)

        with open('maxlen.pickle', 'rb') as maxlen:
            [maxlen_e, maxlen_d] = pickle.load(maxlen)

        with open('indices_word.pickle', 'rb') as i2w:
            indices2word = pickle.load(i2w)

        with open('word_indices.pickle', 'rb') as w2i:
            word2indices = pickle.load(w2i)

        print(word2indices["　"])
        row = encoder.shape[0]

        encoder = encoder.reshape((row, maxlen_e))
        decoder = decoder.reshape((row, maxlen_d))
        label = label.reshape((row, maxlen_d))
        data = {
            'encoder': encoder,
            'decoder': decoder,
            'label': label,
            'maxlen_e': maxlen_e,
            'maxlen_d': maxlen_d,
            'indices2word': indices2word,
            'word2indices': word2indices,
            'input_dim': len(words),
            'output_dim': len(words),
            'words': words
        }
        return data


dataset = load_data()
maxlen_e = dataset['maxlen_e']
maxlen_d = dataset['maxlen_d']
encoder = dataset['encoder']
decoder = dataset['decoder']
label = dataset['label']
indices_word = dataset['indices2word']
word_indices = dataset['word2indices']
words = dataset['words']
data_row = encoder.shape[0]                  # 訓練データの行数
n_split = int(data_row*0.9)           # データの分割比率
# データを訓練用とテスト用に分割
encoder_train, encoder_test = np.vsplit(encoder, [n_split])  # エンコーダインプット分割
decoder_train, decoder_test = np.vsplit(decoder, [n_split])  # デコーダインプット分割
label_train, label_test = np.vsplit(label, [n_split])  # ラベルデータ分割
print(len(label_train))
# train_dataset
