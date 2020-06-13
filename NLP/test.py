from recordCSV import pull_data
import pandas as pd

a = pd.DataFrame()
print(a.shape)

a = pull_data("../data/test.csv")
print(a.shape)

