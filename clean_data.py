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
data_too = []
for index, row in data.iterrows():
    if i['category'] not in ['American Voices', 'Infographic', 'Slideshow', 'Entertainment',
                    'Editorial Cartoon'] and i['category'] is not None:
        data_too = data_too.append(i)
post_title_onion = pd.DataFrame(data_too[['title']])
post_title_onion["onion"] = 1
print(post_title_onion.head())
post_title_onion.to_csv("data/posts_clean.csv")
#ignore no category,  american voices, infographic, slideshow,