class file_util:

    def read_pickle(file_list):
        mat = []
        for i in range(0, len(file_list)):
            with open(file_list[i], 'rb') as f:
                generated_list = pickle.load(f)  #生成リストロード
                mat.extend(generated_list)
                print(i)
                del generated_list
        return mat, generated_list