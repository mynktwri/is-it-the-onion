import csv
import pandas as pd
import numpy as np
from analyze import parse

def pull_data(filename):
    f = pd.read_csv(filename)
    headlines = f["title"]
    onions = f["onion"]
    parsed_titles = [] # list of dataframes
    # pdf = pd.DataFrame()
    for title in headlines:
        print(title)
        parsed_titles.append(parse(title)) #appends one sentence at a time
    # print(parsed_titles)
    pdf = pd.DataFrame(parsed_titles) #convert list into df
    pdf["onion"] = onions[0]
    pdf.to_csv("allData.csv")
    return pdf

#  , cleaned sentence, onion
# 0, datafreame(i fk u eburi day), 1
# 1, etc etc, 1
