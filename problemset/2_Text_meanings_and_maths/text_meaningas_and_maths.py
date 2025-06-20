#%%
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

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

#%% Convert to DataFrame (assuming each article has "text" and "year")
df = pd.DataFrame(articles)
df = df[df['text'].str.strip().astype(bool)]  # remove empty texts

#%% TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=1000, stop_words="english")
X_tfidf = vectorizer.fit_transform(df["text"])

#%% Dimensionality Reduction
# Option A: t-SNE (slower, non-linear, better for local structure)
tsne = TSNE(n_components=2, random_state=38, perplexity=30)
X_reduced_tsne = tsne.fit_transform(X_tfidf.toarray())

# Create plotting DataFrame
df_plot = pd.DataFrame(X_reduced_tsne, columns=["x", "y"])
df_plot["year"] = df["date"]
df_plot["year"] = pd.to_datetime(df_plot["year"].apply(lambda x: x["$date"]), errors="coerce").dt.year

# Plotting
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df_plot, x="x", y="y", hue="year", palette="tab20", alpha=0.7)
plt.title("Document Visualization using TF-IDF + TSNE")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.legend(title="Year")
plt.grid(True)
plt.show()

#%% Option B: PCA (faster, linear)
pca = PCA(n_components=2, random_state=38)
X_reduced_pca = pca.fit_transform(X_tfidf.toarray())

# Create plotting DataFrame
df_plot = pd.DataFrame(X_reduced_pca, columns=["x", "y"])
df_plot["year"] = df["date"]
df_plot["year"] = pd.to_datetime(df_plot["year"].apply(lambda x: x["$date"]), errors="coerce").dt.year

# Plotting
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df_plot, x="x", y="y", hue="year", palette="tab20", alpha=0.7)
plt.title("Document Visualization using TF-IDF + PCA")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.legend(title="Year")
plt.grid(True)
plt.show()


# %%
