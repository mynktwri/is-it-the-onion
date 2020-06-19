from NLP.recordCSV import pull_data
import pandas as pd

print("Running Not Onion data...")
not_onion_df = pull_data("../data/notonion_clean.csv", "notonion_keras_data.npy")
print("Done!")
temp = pd.read_csv("../data/posts_clean.csv")
temp = temp.iloc[:966]
temp.to_csv("../data/onion_clean.csv")
print("Running Onion data...")
onion_df = pull_data("../data/onion_clean.csv", "onion_keras_data.npy")
print("Done!")