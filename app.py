from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load model
model = pickle.load(open("final_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        values = [float(x) for x in request.form.values()]
        prediction = model.predict([values])[0]
        result = "Fraud" if prediction==1 else "Not Fraud"
        return render_template("submit.html", prediction=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
