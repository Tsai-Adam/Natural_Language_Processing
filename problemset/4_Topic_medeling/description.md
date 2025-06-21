# Hidden Themes in Tripadvisor Reviews

## Context

This project analyzes the [`hotel_reviews.csv`](https://github.com/simoneSantoni/NLP-orgs-markets/blob/b13e6442bbf5789da7f41fec21c0f6058fdc4681/sampleData/tripadvisorReviews/hotel_reviews.csv) dataset, which contains 20,491 hotel reviews from Tripadvisor. Each row in the file is a review; the first column contains the review text and the second column contains the associated rating. The goal is to use topic modeling to generate features for training a classifier that distinguishes between ‘bad rating’ reviews (e.g., 1 or 2 stars) and ‘good rating’ reviews (e.g., 4 or 5 stars).

## Problem Statement

- **Objective:**  
  Apply topic modeling to extract latent themes from hotel reviews and use these as features for classification.
- **Methods:**  
  Use [Gensim](https://radimrehurek.com/gensim/), Gensim with [Mallet](https://mimno.github.io/Mallet/index), or [Tomotopy](https://bab2min.github.io/tomotopy/v0.12.2/en/) to:
    - Explore multiple topic models with different numbers of topics.
    - Select the optimal topic model for the task of feature creation for classification.
    - Justify the choice of the best model based on your findings.

## Additional Resources

- [Notion Assignment Page](https://simone-santoni.notion.site/Hidden-themes-in-Tripadvisor-reviews-11b3699c32f34f1b99c032c7cf55e00b)

---
