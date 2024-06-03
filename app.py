from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
run_with_ngrok(app)

# Load the trained model
model = load_model('lstm_model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

maxlen = 100  # Ensure this matches your training setup

def scrape_reviews(imdb_url):
    reviews = []
    response = requests.get(imdb_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    review_divs = soup.find_all('div', class_='text show-more__control')
    for div in review_divs:
        reviews.append(div.get_text())
    
    return reviews

def classify_reviews(reviews, model, tokenizer, maxlen):
    sequences = tokenizer.texts_to_sequences(reviews)
    padded_sequences = pad_sequences(sequences, maxlen=maxlen)
    predictions = model.predict(padded_sequences)
    sentiments = ['positive' if p >= 0.5 else 'negative' for p in predictions]
    return sentiments

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    imdb_url = request.form['url']
    reviews = scrape_reviews(imdb_url)
    sentiments = classify_reviews(reviews, model, tokenizer, maxlen)
    
    positive_count = sentiments.count('positive')
    negative_count = sentiments.count('negative')
    
    recommendation = 'recommended' if positive_count > negative_count else 'not recommended'
    
    return render_template('result.html', positive_count=positive_count, negative_count=negative_count, recommendation=recommendation)

if __name__ == '__main__':
    app.run()
