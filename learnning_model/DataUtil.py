class DataUtil:

    # データをバッチ化するための関数
    def train2batch(input_data, output_data, batch_size):
        input_batch = []
        output_batch = []
        input_shuffle, output_shuffle = shuffle(input_data, output_data)
        for i in range(0, len(input_data), batch_size):
            input_batch.append(input_shuffle[i:i + batch_size])
            output_batch.append(output_shuffle[i:i + batch_size])
        return input_batch, output_batch
