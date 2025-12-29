import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'text': [
        'Government announces new education policy',
        'Aliens have landed on Earth',
        'Scientists discover new planet',
        'Drinking bleach cures diseases',
        'Elections conducted peacefully'
    ],
    'label': ['Real', 'Fake', 'Real', 'Fake', 'Real']
}

df = pd.DataFrame(data)

# Convert labels
df['label'] = df['label'].map({'Real': 1, 'Fake': 0})

# Text vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# User input
user_input = input("\nEnter a news sentence: ")
input_vector = vectorizer.transform([user_input])
prediction = model.predict(input_vector)

if prediction[0] == 1:
    print("Result: Real News")
else:
    print("Result: Fake News")
