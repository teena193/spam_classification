
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder

import os

def spam_detection():
    file_path = os.environ.get('DATA_FILE_PATH', 'spam.csv')
    
    df = pd.read_csv(file_path) #if running in docker
    # Use LabelEncoder to convert 'Category' column to numerical labels
    label_encoder = LabelEncoder()
    df['label'] = label_encoder.fit_transform(df['Category'])
    # Map 'ham' as 1 and 'spam' as 0
    df['label'] = df['label'].map({0: 1, 1: 0})

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['Message'], df['label'], test_size=0.2, random_state=42)

    # Create a Naive Bayes classifier pipeline
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)

    return model



