
# Movie Sentiment Analysis System

## Overview
This project aims to analyze movie reviews from IMDB and determine their sentiment (positive or negative) using a Long Short-Term Memory (LSTM) model. The system includes a web application where users can input an IMDB movie URL, scrape reviews, and perform sentiment analysis to provide a recommendation based on the overall sentiment.

## Features
- **Sentiment Analysis Model**: Uses an LSTM model trained on the IMDB dataset.
- **Web Scraping**: Extracts reviews from IMDB movie URLs.
- **Real-Time Analysis**: Classifies reviews as positive or negative and provides a recommendation.
- **User-Friendly Interface**: Simple web interface for easy interaction.

## Technologies Used
- **Python** 🐍
- **TensorFlow/Keras** for building and training the LSTM model.
- **Flask** for the web application.
- **BeautifulSoup** for web scraping.

## Setup Instructions

### Prerequisites
- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-sentiment-analysis.git
    cd movie-sentiment-analysis
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Place the pre-trained model and tokenizer in the project directory:
    - `lstm_model.h5`
    - `tokenizer.pkl`

### Running the Application
1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000`.

### Usage
1. Enter the URL of an IMDB movie page.
2. Click the "Analyze" button to scrape reviews and perform sentiment analysis.
3. View the results, including the count of positive and negative reviews and the recommendation.

## Project Structure
```
movie-sentiment-analysis/
├── app.py                # Flask application
├── lstm_model.h5         # Pre-trained LSTM model
├── tokenizer.pkl         # Tokenizer used for preprocessing
├── templates/
│   ├── index.html        # Home page template
│   └── result.html       # Result page template
├── requirements.txt      # Python dependencies
└── README.md             # Project README file
```
