# Classifying Helpful and Unhelpful IMDB Reviews

## Context

You are tasked with adjudicating between helpful and unhelpful movie reviews from the IMDB database. The goal is to classify each movie review into one of two categories:
- **0 / not helpful:** Less than 30% of IMDB users found the review helpful
- **1 / helpful:** More than 70% of IMDB users found the review helpful

## Data and File Description

- **train.csv**  
  Contains 10,755 labeled reviews.  
  - Column `helpfulness_cat`: the label (0 or 1)
  - Column `imdb_user_review`: the review text

- **test.csv**  
  Contains 5,071 unlabeled reviews.  
  - Column `_id`: unique review identifier  
  - Column `imdb_user_review`: the review text to classify

- **submission.csv**  
  The file you will generate for submission:  
  - Column `_id`: review identifier  
  - Column `helpfulness_cat`: your predicted label (0 or 1)  
  **Note:**  
    - Use the exact headers `_id,helpfulness_cat` in your submission  
    - Only use the `_id` values included in test.csv

## Download

Dataset and submission template available here:  
[Dropbox download link](https://www.dropbox.com/scl/fo/b6wk88badiapwvdst5t5c/h?dl=0&rlkey=2cisp5b55962dar4vded3ijre)

## Guidelines

You may use **any classifier or combination of classifiers**, any selection of features, and either supervised, semi-supervised, or transfer learning approaches.

- **Features** may include (but are not limited to):
  - Bag-of-Words (BoW) vectors
  - TFIDF vectors
  - Embedding-based vectors
  - Topic-to-document probabilities

- **Estimators:**  
  You can use logistic regression, Naive Bayes, or any estimator suitable for the task.

## Additional Resources

- [Notion Assignment Page](https://simone-santoni.notion.site/Classifying-helpful-and-unhelpful-IMDB-reviews-2d060f5f9ddf44c5b6b5eb83a7608766)

---
