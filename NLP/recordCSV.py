import csv
import pandas as pd
import numpy as np
from analyze import parse


def save_data(text):
    parse_text = parse(text)
    return parse_text


def pull_data(filename):
    f = pd.read_csv(filename)
    headlines = f["title"]
    parsed_titles = []
    for title in headlines:
        print(title)
        parsed_titles.append(save_data(title))

    pdf = pd.DataFrame(parsed_titles)
    pdf.to_csv("allData.csv")