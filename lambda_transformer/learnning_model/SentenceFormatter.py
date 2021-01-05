import re
import MeCab
import numpy as np


class SentenceFormatter:

    def morphological_analysis(self, text):
        wakati = MeCab.Tagger('-O wakati -r /dev/null -d /mnt/lambda/lib/mecab/dic/ipadic')
        ret = []
        text = self.remove_special_character(text)
        result = wakati.parse(text).split()  # これでスペースで単語が区切られる
        for mrph in result:
            ret += self.modification(mrph)
        return ret

    def remove_special_character(self, text):
        # 改行、半角スペース、全角スペースを削除
        text = re.sub('\r', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('　', '', text)
        text = re.sub(' ', '', text)

        # 数字文字の一律「0」化
        text = re.sub(r'[0-9 ０-９]', '0', text)  # 数字

        return text

    # 前処理とJanomeの単語分割を合わせた関数を定義する
    def modification(self, word):
        modified = [word]
        return modified

    def text_to_vector(self, texts, datasets):
        word_indices = datasets["word2indices"]
        texts = self.morphological_analysis(texts)
        mat_urtext = np.zeros((75, 1), dtype=int)
        for i in range(0, len(texts)):
            if texts[i] in word_indices:  # 出現頻度の低い単語のインデックスをunkのそれに置き換え
                mat_urtext[i, 0] = word_indices[texts[i]]
            else:
                mat_urtext[i, 0] = word_indices['UNK']

        for i in range(len(texts), 75, 1):
            mat_urtext[i, 0] = 0

        print(mat_urtext.shape)
        return mat_urtext
