# 🎬 Movie Review Sentiment Analyzer
This is a Flask web application that uses a pre-trained BiLSTM model to analyze the sentiment of movie reviews. Users can submit reviews, see predictions (positive/negative), view previously submitted reviews, and delete any review. The model is trained on the IMDB movie review dataset.

# 🚀 Features
Analyze sentiment (positive/negative) of movie reviews using a BiLSTM model.
Search and filter previously submitted reviews.
Delete any review from the list.
Clean, simple interface with Flask templating.


# 🧠 Model Information
Model: BiLSTM (Bidirectional Long Short-Term Memory)
Framework: TensorFlow / Keras
Tokenizer: Trained and saved using Keras Tokenizer
Input Length: 200 tokens (padded)

# 📁 Project Structure

.
├── app.py                 # Main Flask application
├── imdb_sentiment_bilstm.h5   # Trained sentiment analysis model
├── tokenizer.pkl          # Tokenizer used during training
├── templates/
│   ├── index.html         # Main input page
│   ├── guide.html         # User guide
│   └── reviews.html       # Review list page
├── static/                # CSS, images, or JS files (optional)
└── README.md              # Project documentation

###  🛠️ Installation & Setup

# Create a virtual environment 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:



# Run the application:
python app.py
Open in browser:
http://127.0.0.1:5000


# 💡 Usage
Go to the home page.
Enter a movie name and a review.
Click Submit to see the sentiment result.
Navigate to the Reviews page to see all reviews.
Use the search bar to filter results.
Click Delete to remove a review.
