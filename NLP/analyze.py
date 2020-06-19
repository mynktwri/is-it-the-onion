import spacy
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from keras.utils import to_categorical
# from keras.preprocessing.sequence import pad_sequences

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_md") # medium spaCy word base

# "text", "POS", "stopword" are parsed for now
# param text is a whole sentence as a string
def parse(text):
    doc = nlp(text)
    parse_list = np.zeros(shape=(40, 300)) #prepadding everything w zEROS
    POS_list = np.zeros(shape=(40,))
    for t in doc:
        wordvec = pd.Series(t.vector)
        POS_list[t.i] = convert_pos(t.pos_)
        parse_list[t.i] = wordvec.to_numpy(dtype='float16', copy=True) #one word's vector representation and POS
    # print(parse_list.to_numpy(dtype='float16', copy=True))
    # numpy_parse_list = pad_sequences(numpy_parse_list, padding='post', maxlen=40)
    arr = np.arange(1, 19, 1)
    encoded = to_categorical(POS_list, num_classes=20)[:, 1:]
    # print(np.concatenate((parse_list, OneHotEncoder(POS_list)), axis=1))
    return np.concatenate((parse_list, encoded), axis=1)
    # returnes one sentence at a time as a 1 DIMENSIONal numpy array - vector representation, POS

    #has to be (40,301) in shape
def convert_pos(pos):
    pos_list = {
        "ADJ": 1,
        "ADP": 2,
        "ADV": 3,
        "AUX": 4,
        "CONJ": 5,
        "CCONJ": 6,
        "DET": 7,
        "INTJ": 8,
        "NOUN": 9,
        "NUM": 10,
        "PART": 11,
        "PRON": 12,
        "PROPN": 13,
        "PUNCT": 14,
        "SCONJ": 15,
        "SYM": 16,
        "VERB": 17,
        "SPACE": 18
    }
    if pos not in pos_list:
        return 19
    else:
        return pos_list[pos]


def convert_stop(bool):
    if bool:
        return 1
    else:
        return 0
