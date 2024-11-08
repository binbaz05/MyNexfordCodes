# Importing necessary libraries
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 1. Loading the cancer dataset

data = load_breast_cancer()
X = data.data
y = data.target

# Converting data to DataFrame

df = pd.DataFrame(X, columns=data.feature_names)

df['target'] = y

# 2. PCA Implementation: Reducing dataset to 2 PCA components

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print(f"\n","Explained Variance Ratio by PCA Components:", pca.explained_variance_ratio_ ,"\n")

print(f"\n","Sum of Explained Variance Ratio (should be close to 1):", sum(pca.explained_variance_ratio_), "\n")

# 3. Bonus: Logistic Regression for prediction on PCA-reduced data

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.3, random_state=42)

# Initialize and fit the Logistic Regression model

log_reg = LogisticRegression()

log_reg.fit(X_train, y_train)

# Predict on test set

y_pred = log_reg.predict(X_test)

# Evaluate the model

accuracy = accuracy_score(y_test, y_pred)
print(f"\n","Accuracy of Logistic Regression on transformed data:", accuracy,"\n")
