# natural_language_processing.py

import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn as nn
import torch.optim as optim

# Load the dataset
df = pd.read_csv('dataset.csv')

# Preprocess the text data
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

df['text'] = df['text'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)

# Train a Logistic Regression classifier
lr_classifier = LogisticRegression(max_iter=1000)
lr_classifier.fit(X_train_tfidf, y_train)

# Train a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100)
rf_classifier.fit(X_train_tfidf, y_train)

# Train a Support Vector Machine classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_tfidf, y_train)

# Train a BERT-based classifier
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=8)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-5)

for epoch in range(5):
    model.train()
    total_loss = 0
    for batch in X_train:
        input_ids = tokenizer.encode(batch, return_tensors='pt').to(device)
        labels = torch.tensor(y_train).to(device)
        optimizer.zero_grad()
        outputs = model(input_ids, labels=labels)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f'Epoch {epoch+1}, Loss: {total_loss / len(X_train)}')

model.eval()

# Evaluate the classifiers
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    print('Confusion Matrix:')
    print(confusion_matrix(y_test, y_pred))

evaluate_classifier(nb_classifier, X_test_tfidf, y_test)
evaluate_classifier(lr_classifier, X_test_tfidf, y_test)
evaluate_classifier(rf_classifier, X_test_tfidf, y_test)
evaluate_classifier(svm_classifier, X_test_tfidf, y_test)

# Use the BERT-based classifier to make predictions
def make_prediction(text):
    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)
    outputs = model(input_ids)
    _, predicted = torch.max(outputs.scores, dim=1)
    return predicted.item()

print(make_prediction('This is a sample text'))
