import pickle

class modified_sentence:
    # 品詞分解
    def decomposition(file, jumanpp):
        f = open(file, 'r')
        df1 = csv.reader(f)
        data = [v for v in df1]
        print('number of rows :', len(data))
        
        parts = []
        for i in range(len(data)):
            data[i][0] = data[i][0].replace(' ', '')
            if len(data[i][0].encode('utf-8')) <= 4096:
                result = jumanpp.analysis(data[i][0])
            else:
                print(i, ' skip')
                continue
            for mrph in result.mrph_list():
                parts += modification(mrph.midasi)
            if i % 5000 == 0:
                print(i)
                
        return parts

    from __future__ import unicode_literals

    def remove_REQRES(source_csv, list_corpus):
        with codecs.open(source_csv, "rb") as f:
            df2 = pickle.load(f)
            mat = [line for line in df2]
            j = 0
            #補正
            for i in range(0, len(mat)):
                if len(mat[i]) != 0:
                    if mat[i] != '':
                        if mat[i] != '@' and mat[i] != 'EOS' and mat[i] != ':' and mat[i] != '\\' :
                            if mat[i] == 'REQ' and mat[i + 1] == ':':  #デリミタ「REQ:」対応
                                list_corpus.append('REQREQ')
                            elif mat[i] == 'RES' and mat[i + 1] == ':':  #デリミタ「RES:」対応
                                list_corpus.append('RESRES')
                            else:
                                list_corpus.append(mat[i])
                            if i % 1000000 == 0:
                                print(i, list_corpus[j])
                            j += 1
        print(len(list_corpus))
        del mat
        return
        
    # coding: utf-8
    def generate_mat():
        file_list = glob.glob('list_corpus/*')
        print('ファイル数 =', len(file_list))
        mat = []
        for i in range(0, len(file_list)):
            with open(file_list[i], 'rb') as f:
                generated_list = pickle.load(f)  #生成リストロード
                mat.extend(generated_list)
                print(i)
                del generated_list
                
        mat.append('REQREQ')
        print("len(mat)", len(mat))
        
        words = sorted(list(set(mat)))
        cnt = np.zeros(len(words))
        
        print('total words:', len(words))
        word_indices = dict((w, i) for i, w in enumerate(words))  #単語をキーにインデックス検索
        indices_word = dict((i, w) for i, w in enumerate(words))  #インデックスをキーに単語を検索
        
        #単語の出現数をカウント
        for j in range(0, len(mat)):
            cnt[word_indices[mat[j]]] += 1
        #出現頻度の少ない単語を「UNK」で置き換え
        words_unk = []  #未知語一覧
        for k in range(0, len(words)):
            if cnt[k] <= 0:
                words_unk.append(words[k])
                words[k] = 'UNK'
                
        print('words_unk:', len(words_unk))  # words_unkはunkに変換された単語のリスト
        
        #低頻度単語をUNKに置き換えたので、辞書作り直し
        words = list(set(words))
        words.append('\t')  #０パディング対策。インデックス０用キャラクタを追加
        words = sorted(words)
        print('new total words:', len(words))
        word_indices = dict((w, i) for i, w in enumerate(words))  #単語をキーにインデックス検索
        indices_word = dict((i, w) for i, w in enumerate(words))  #インデックスをキーに単語を検索
        
        #単語インデックス配列作成
        mat_urtext = np.zeros((len(mat), 1), dtype=int)
        for i in range(0, len(mat)):
            if mat[i] in word_indices:  #出現頻度の低い単語のインデックスをunkのそれに置き換え
                mat_urtext[i, 0] = word_indices[mat[i]]
            else:
                mat_urtext[i, 0] = word_indices['UNK']
                
        print(mat_urtext.shape)
        #作成した辞書をセーブ
        with open('word_indices.pickle', 'wb') as f:
            pickle.dump(word_indices, f)
            
        with open('indices_word.pickle', 'wb') as g:
            pickle.dump(indices_word, g)
        
        #単語ファイルセーブ
        with open('words.pickle', 'wb') as h:
            pickle.dump(words, h)
            print(len(words))
        
        #コーパスセーブ
        with open('mat_urtext.pickle', 'wb') as ff:
            pickle.dump(mat_urtext , ff)    
