import spacy
from spacy import displacy
import pandas as pd

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")


# "text", "lemma", "POS", "explain", "stopword" are parsed for now
def parse(text):
    doc = nlp(text)
    parse_list = []
    for t in doc:
        row = [t.text, t.pos_, t.is_stop]
        parse_list.append(row)
    pd.DataFrame(parse_list)
    return parse_list

# Load English tokenizer, tagger, parser, NER and word vectors
# doc = nlp("Brad Pitt took an SAT test and I think i love tests")
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# for entity in doc.ents:
#     print(entity.text, entity.label_)
