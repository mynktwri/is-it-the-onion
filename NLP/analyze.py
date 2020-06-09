import spacy
import pandas as pd

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")


# "text", "POS", "stopword" are parsed for now
def parse(text):
    doc = nlp(text)
    parse_list = []
    for t in doc:
        row = [t.text, convert_pos(t.pos_), convert_stop(t.is_stop)]
        parse_list.append(row)
    pd.DataFrame(parse_list)
    return parse_list


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
