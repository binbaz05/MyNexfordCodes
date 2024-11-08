This project uses Principal Component Analysis (PCA) and Logistic Regression to build a model that predicts patient referrals at Anderson Cancer Center.
The number of referrals is said to have been on an increase and this model will hopefully help to strealine the referral process.

PCA Implementation: Reduces the dataset into two main components, preserving the most important variables, making the data easier to manage and visualize.
Logistic Regression: A classification model is used to predict whether a patient needs a referral based on key features derived from PCA.

Requirements:
    Python 3.x
    Libraries: sklearn, pandas
You can install the necessary libraries using: "pip install scikit-learn pandas"

Dataset:
The dataset used is the Breast Cancer Wisconsin (Diagnostic) Dataset, which is available directly through sklearn.datasets. It contains 30 features related to cancer diagnostics, with the target being either malignant or benign.

Code Outline:

1.  Loading the Dataset
    The Breast Cancer dataset is loaded and converted to a DataFrame for clarity.

2. PCA Implementation (Dimensionality Reduction)
    We perform PCA to reduce the dataset features to 2 principal components.
    The explained variance ratio for each component is printed to understand how much variance each component captures. 

3.  Optional Logistic Regression Model
    A logistic regression model is applied to classify the data after PCA transformation.
    The dataset is split into training and testing sets, and the accuracy of the logistic regression model on the PCA-reduced data is calculated.

Key Outputs:

    Explained Variance Ratio: Displays the amount of variance explained by each of the two PCA components.
    Logistic Regression Accuracy: The accuracy score reflects how well logistic regression performs on the reduced data, indicating the effectiveness of dimensionality reduction for classification.

Usage:
    To run the program: 
    python PCA.py



