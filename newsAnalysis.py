import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string

nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([word.lower() for word in text.split() if word.lower() not in stop_words])
    return text

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['processed_text'] = df['text'].apply(preprocess)
    return df

# df = load_data("TrumpAtMcDonalds/APTrumpMcDonalds.txt")

# sia = SentimentIntensityAnalyzer()

# def get_sentiment(text):
#     score = sia.polarity_scores(text)
#     if score['compound'] >= 0.05:
#         return "positive"
#     elif score['compound'] <= -0.05:
#         return "negative"
#     else:
#         return "neutral"

# df['initial_sentiment'] = df['processed_text'].apply(get_sentiment)


print(load_data("TrumpAtMcDonalds/APTrumpMcDonalds.txt"))
