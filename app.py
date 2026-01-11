from flask import Flask, render_template, request
import numpy as np
import pickle

# loading model
model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

# flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = request.form['feature']
        features = features.split(',')
        np_features = np.asarray(features, dtype=np.float32)
        np_features = scaler.transform(np_features.reshape(1, -1))

        # prediction
        pred = model.predict(np_features)
        message = ['Cancerous' if pred[0] == 1 else 'Not Cancerous']
        return render_template('index.html', message=message)
    except Exception as e:
        message = ['Error: Please enter 31 valid numerical features separated by commas.']
        return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
