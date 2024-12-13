from flask import Flask, render_template, request
from diamond_model import predict_price  # Ensure this file is in the same directory as app.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        carat = float(request.form["carat"])
        cut = int(request.form["cut"])
        size = float(request.form["size"])

        predicted_price = predict_price(carat, cut, size)
        return render_template("result.html", price=predicted_price)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
