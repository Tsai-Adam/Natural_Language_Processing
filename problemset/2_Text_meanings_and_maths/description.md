# Mapping Documents onto the Vector Space

## Context

This project uses the [`ai_in_finance.json`](https://github.com/simoneSantoni/NLP-orgs-markets/blob/master/sampleData/econNewspaper/ai_in_finance.json) dataset, which contains over 4,000 articles on AI and financial services from The Wall Street Journal and The Financial Times.

For more information about the dataset, refer to:  
[Lanzolla, Gianvito, Simone Santoni, and Christopher Tucci. "Unlocking value from AI in financial services: strategic and organizational tradeoffs vs. media narratives." In Artificial Intelligence for Sustainable Value Creation. Edward Elgar Publishing, 2021.](https://github.com/simoneSantoni/NLP-orgs-markets/blob/46dad729070a5125c95adc214abbec312cae7077/sampleData/econNewspaper/lanzolla_santoni_tucci.pdf)

## Problem Statement

- **Objective:**  
  Transform each document (article) in the corpus into a vector using either the Bag-of-Words (BoW) or TF-IDF approach.
- **Visualization:**  
  Apply a dimensionality reduction technique (such as PCA, t-SNE, or UMAP—see [scikit-learn manifold documentation](https://scikit-learn.org/stable/modules/manifold.html)) to project the high-dimensional vectors into 2D or 3D space.
- **Bonus:**  
  Color-code the document positions in the visualization based on document-level attributes (e.g., year of publication).

## Additional Resources

- [Notion Assignment Page](https://simone-santoni.notion.site/Mapping-documents-onto-the-vector-space-c6bbfb18c6a0443ab3525005d4a3c250)

---
