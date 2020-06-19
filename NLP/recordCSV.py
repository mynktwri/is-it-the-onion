import csv
import pandas as pd
import numpy as np
from NLP.analyze import parse

def pull_data(filename, filename_out):
    f = pd.read_csv(filename)
    headlines = f["title"]
    onions = f["onion"]
    parsed_titles = np.ndarray(shape=(headlines.size, 40, 319))# list of sentences
    targets = np.zeros(shape=(headlines.size, 1, 1)) #list of targets
    print(parsed_titles.shape)
    # pdf = pd.DataFrame()
    for index, row in f.iterrows():
        # print(f[index])
        parsed_titles[index] = parse(row['title'])#appends one sentence at a time

    # print(parsed_titles)
    # pdf = pd.DataFrame(parsed_titles) #convert list into df
    # pdf[] = onions[0]

    np.save(filename_out, parsed_titles, allow_pickle=False)
    return parsed_titles

#  , cleaned sentence, onion
# 0, datafreame(i fk u eburi day), 1
# 1, etc etc, 1
