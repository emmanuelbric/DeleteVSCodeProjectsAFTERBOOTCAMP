import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temperature = float(request.form.get('temperature'))
        prediction = model.predict([[temperature]])
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_text=f'Total revenue generated is Rs. {output}/-')
    except ValueError:
        return render_template("index.html", prediction_text='Invalid input: please enter a numeric value for temperature.')

if __name__ == "__main__":
    app.run(debug=True)
