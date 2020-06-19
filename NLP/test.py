from recordCSV import pull_data
import pandas as pd
import numpy as np

a = pd.DataFrame()
print(a.shape)

a = pull_data("../data/test.csv", "../data/test_out.npy")
print(a.shape)
a = np.load("../data/test_out.npy")
print(a[:])
