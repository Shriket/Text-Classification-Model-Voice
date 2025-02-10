# Text-Classification
Text Classification for Active vs. Passive Voice Detection

Deployment link :- [textclassificationmodelvoice](https://textclassificationmodelvoice.streamlit.app/)

### Demo:
![Demo GIF](https://github.com/Shriket/Text-Classification-Model-Voice/raw/main/Demo.gif)



**🔍 Introduction**

This model is designed to detect active vs. passive voice in text using machine learning techniques 🤖. The problem of active vs. passive voice detection is an important task in natural language processing, as it can help improve the clarity and readability of text.

**📈 Technologies and Tools**

The notebook utilizes Python as the primary programming language, along with several popular libraries and tools, including:

*   `pandas` for data manipulation and analysis
*   `scikit-learn` for machine learning tasks, such as feature extraction and model training
*   `CountVectorizer` for text vectorization
*   `LogisticRegression`, `SVC`, and `DecisionTreeClassifier` for text classification

**📝 Step-by-Step Explanation**

### 📄 Code Block 1: Importing Libraries and Loading Data

*   Purpose: Load necessary libraries and import the dataset.
*   Key steps:
    *   Import `pandas` and `scikit-learn` libraries.
    *   Load the dataset from an Excel file (`immverse_ai_eval_dataset.xlsx`) using `pd.read_excel`.
*   Results: The dataset is loaded into a Pandas DataFrame.

### 📄 Code Block 2: Data Preprocessing

*   Purpose: Preprocess the data by converting the `voice_Passive` column to integer values.
*   Key steps:
    *   Use the `astype` method to convert the `voice_Passive` column to integer values.
*   Results: The `voice_Passive` column is converted to integer values.

### 📄 Code Block 3: Data Split and Vectorization

*   Purpose: Split the data into training and testing sets, and vectorize the text data using `CountVectorizer`.
*   Key steps:
    *   Split the data into training and testing sets using `train_test_split`.
    *   Create a `CountVectorizer` object and fit it to the training data.
    *   Transform the training and testing data using the `CountVectorizer` object.
*   Results: The data is split into training and testing sets, and the text data is vectorized.

### 📄 Code Block 4: Model Training and Evaluation

*   Purpose: Train and evaluate machine learning models for text classification 🤖.
*   Key steps:
    *   Train a `LogisticRegression` model on the training data.
    *   Train an `SVC` model on the training data.
    *   Train a `DecisionTreeClassifier` model on the training data.
    *   Evaluate the models using accuracy score and confusion matrix.
*   Results: The models are trained and evaluated, and the results are displayed.

### 📄 Code Block 5: Model Comparison and Selection

*   Purpose: Compare the performance of the trained models and select the best one 🏆.
*   Key steps:
    *   Compare the accuracy scores of the trained models.
    *   Select the model with the highest accuracy score.
*   Results: The best-performing model is selected. (Note: This step is *not* actually implemented in the provided notebook code. The code trains and saves the `LogisticRegression` model regardless of its performance compared to the others.)

### 📄 Code Block 6: Side-by-Side Comparison of Actual and Predicted Values

*   Purpose: Compare the actual and predicted values side-by-side.
*   Key steps:
    *   Create a Pandas DataFrame to store the actual and predicted values.
    *   Display the DataFrame.
*   Results: The actual and predicted values are displayed side-by-side.

**📈 Data**

The dataset used in this notebook is a custom dataset, which is not publicly available. The dataset contains text data with corresponding labels (active or passive voice). The dataset is stored in an Excel file (`immverse_ai_eval_dataset.xlsx`).

**🤖 Model**

The notebook uses three machine learning models for text classification:

*   `LogisticRegression`
*   `SVC`
*   `DecisionTreeClassifier`

The models are trained on the vectorized text data, and their performance is evaluated using accuracy score and confusion matrix.

**📊 Results and Evaluation**

The models are evaluated using accuracy score and confusion matrix. The results show that the `LogisticRegression` model performs the best, with an accuracy score of 0.9356 🏆.

**📝 Conclusion**

In this notebook, we demonstrated the use of machine learning techniques for detecting active vs. passive voice in text. We trained and evaluated three machine learning models, and selected the best-performing model 🏆.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/6518087/83bdae6c-1599-4c60-9064-596c6d84eafa/programme.ipynb

---
Answer from Perplexity: pplx.ai/share
