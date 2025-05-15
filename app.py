from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['temperature']),
            float(request.form['rh']),
            float(request.form['ws']),
            float(request.form['rain']),
            float(request.form['ffmc']),
            float(request.form['dmc']),
            int(request.form['classes'])
        ]
        mock_prediction = (features[0] * 0.1 +
                          features[1] * 0.05 +
                          features[2] * 0.2 +
                          features[3] * 0.15 +
                          features[4] * 0.25 +
                          features[5] * 0.1 +
                          features[6] * 5)
        prediction = round(mock_prediction, 2)
        return render_template('result.html', prediction=prediction, features=features)
    except Exception as e:
        return render_template('error.html', error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)