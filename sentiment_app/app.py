from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load trained model and tokenizer
model = tf.keras.models.load_model("imdb_sentiment_bilstm.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_len = 200  # must match training
reviews_list = []  # in-memory storage

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    movie = request.form.get("movie")
    text = request.form.get("review")

    # Preprocess
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_len)
    prediction = model.predict(padded)[0][0]
    sentiment = "Positive 😀" if prediction > 0.5 else "Negative 😞"

    # Assign ID and save review
    review_id = len(reviews_list) + 1
    reviews_list.append({
        "id": review_id,
        "movie": movie,
        "text": text,
        "sentiment": sentiment
    })

    return render_template("index.html", prediction=sentiment)

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/reviews", methods=["GET"])
def reviews():
    search_query = request.args.get("search", "").lower()
    if search_query:
        filtered = [r for r in reviews_list if search_query in r["movie"].lower() or search_query in r["text"].lower()]
        return render_template("reviews.html", reviews=filtered)
    return render_template("reviews.html", reviews=reviews_list)

@app.route("/delete_review", methods=["POST"])
def delete_review():
    review_id = int(request.form.get("review_id"))
    global reviews_list
    reviews_list = [r for r in reviews_list if r.get("id") != review_id]
    return redirect(url_for("reviews"))

if __name__ == "__main__":
    app.run(debug=True)
