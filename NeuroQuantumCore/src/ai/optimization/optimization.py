# optimization.py

import numpy as np
from scipy.optimize import minimize
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the objective function to optimize
def objective(params):
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return -accuracy_score(y_test, y_pred)

# Define the bounds for the hyperparameters
bounds = {
    'n_estimators': (10, 100),
    'max_depth': (5, 20),
    'min_samples_split': (2, 10),
    'min_samples_leaf': (1, 10)
}

# Perform the optimization using the minimize function from scipy
res = minimize(objective, [50, 10, 2, 1], method='SLSQP', bounds=list(bounds.values()))

# Print the optimized hyperparameters
print('Optimized hyperparameters:', res.x)

# Train a model with the optimized hyperparameters
model = RandomForestClassifier(**dict(zip(bounds.keys(), res.x)))
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Perform grid search for hyperparameter tuning
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'poly']
}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and the corresponding score
print('Best hyperparameters:', grid_search.best_params_)
print('Best score:', grid_search.best_score_)

# Train a model with the best hyperparameters
model = SVC(**grid_search.best_params_)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Perform dimensionality reduction using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Perform dimensionality reduction using t-SNE
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

# Plot the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.title('PCA')

plt.subplot(1, 2, 2)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.title('t-SNE')

plt.show()

# Perform clustering using K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Print the cluster labels
print('Cluster labels:', kmeans.labels_)

# Perform clustering using Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# Print the cluster labels
print('Cluster labels:', gmm.predict(X))
