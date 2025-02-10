# Text Classification model for Active vs. Passive Voice Detection

------

Deployment link :- [textclassificationmodelvoice](https://textclassificationmodelvoice.streamlit.app/)

### Demo:
![Demo GIF](https://github.com/Shriket/Text-Classification-Model-Voice/raw/main/Demo.gif)

---------

## Overview

This project implements a machine learning model to classify sentences as either active or passive voice. It leverages NLP techniques for feature extraction and trains several classification algorithms to achieve high accuracy. The goal is to automatically identify voice in text.

------------

## Key Features

-   **Dataset:** Utilizes the `immverse_ai_eval_dataset.xlsx` dataset containing labeled sentences.
-   **Feature Extraction:** Employs `CountVectorizer` to convert text data into numerical features based on word frequencies.
-   **Models Trained:**
    -   Logistic Regression
    -   Support Vector Machine (SVM)
    -   Decision Tree
-   **Evaluation Metric:** Model performance is evaluated using accuracy score on a held-out test set.
-   **Model Persistence:** The trained model is saved for future use, using pickle.

---------------

## Performance

The **Decision Tree** model achieved an accuracy of 0.9356 on the test dataset. This makes it a suitable choice for practical applications.

--------------------

## Files
-   `programme.ipynb`: Jupyter Notebook containing the complete code.
-   `immverse_ai_eval_dataset.xlsx`: The dataset used in this notebook is a custom dataset, which is not publicly available. The dataset contains text data with corresponding labels (active or passive voice). The dataset is stored in an Excel file.

--------------------------------------------------------------------------------------




