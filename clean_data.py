import pandas as pd
import numpy as np

data = pd.read_csv("data/nottheonion.csv")

print(data.head())
post_title_not_onion = pd.DataFrame(data[['post_Title']])

post_title_not_onion["onion"] = 0



print(post_title_not_onion.head())

post_title_not_onion.to_csv("notonion_clean.csv")

data = pd.read_csv("data/posts_filtered.csv")
print(data.head())
post_title_onion = pd.DataFrame(data[['title']])
post_title_onion["onion"] = 1
print(post_title_onion.head())
#ignore no category,  american voices, infographic, slideshow,