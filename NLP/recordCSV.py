import csv
import pandas as pd
import numpy as np
from analyze import parse


def save_data(text):
    parse_text = parse(text)
    # change the w to a to add on.
    df = pd.DataFrame(parse_text)
    df.to_csv('allData.csv', index=False)


def pull_data(filename):
    f = pd.read_csv(filename)
    f.