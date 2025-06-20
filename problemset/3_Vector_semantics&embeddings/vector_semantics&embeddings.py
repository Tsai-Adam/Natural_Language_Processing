#%%
import json


#%% Load the JSON corpus
articles = []
with open("ai_in_finance.json", "r") as f:
    for line in f:
        try:
            article = json.loads(line)
            articles.append(article)
        except json.JSONDecodeError as e:
            print(f"skip the error: {e}")

# Check
print(f"success load {len(articles)} articles")

#%%


#%%

