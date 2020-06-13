import numpy as np
import pandas as pd

def create_embedding_matrix(filepath, word_index, embedding_dim):
    vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
    embedding_matrix = np.zeros((vocab_size, embedding_dim))

    with open(filepath) as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word]
                embedding_matrix[idx] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]

    return embedding_matrix


data = pd.read_csv("data/notonion_clean.csv", index_col=0)
print(data.head())




#set embedding_dim to 50 to start
#nonzero_elements = np.count_nonzero(np.count_nonzero(embedding_matrix, axis=1))
#nonzero_elements / vocab_size

#see how good percent coverage is of the embeddingm atricxxx
