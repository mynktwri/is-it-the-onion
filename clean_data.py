import pandas as pd
import numpy as np

data = pd.read_csv("data/nottheonion.csv")

print(data.head())
post_title_not_onion = pd.DataFrame(data[['post_Title']])

post_title_not_onion["onion"] = 0



print(post_title_not_onion.head())

post_title_not_onion.to_csv("notonion_clean.csv")

data = pd.read_csv("data/posts.csv")
print(data.head())
# data = data[:1000]
data_too = pd.DataFrame()
temp = []
for index, row in data.iterrows():
    if row['category'] not in ['American Voices', 'Infographic', 'Slideshow', 'Entertainment',
                    'Editorial Cartoon'] and row['category'] is not None:
            temp.append(data.iloc[index])
data_too = data_too.append(temp, ignore_index=True)
post_title_onion = data_too.reset_index(drop=True)
post_title_onion["onion"] = 1
post_title_onion.drop(columns=['category', 'date', 'time'], inplace=True)
print(post_title_onion.head())
post_title_onion.to_csv("data/posts_clean.csv")
#ignore no category,  american voices, infographic, slideshow,