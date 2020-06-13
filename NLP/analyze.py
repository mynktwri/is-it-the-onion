import spacy
import pandas as pd
import numpy as np

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_md") # large spacy word base

# "text", "POS", "stopword" are parsed for now
# param text is a whole sentence as a string
def parse(text):
    doc = nlp(text)
    parse_list = pd.DataFrame()
    for t in doc:
        wordvec = pd.Series(t.vector)
        wordvec = wordvec.append(pd.Series(convert_pos(t.pos_)), ignore_index=True)
        parse_list = parse_list.append(wordvec, ignore_index=True) #one word's vector representation and POS
    print(parse_list.to_numpy(dtype='float16', copy=True))
    return parse_list.to_numpy(dtype='float16', copy=True)
    # returnes one sentence at a time as a numpy array - vector representation, POS


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
