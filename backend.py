from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

preprocessor = joblib.load('preprocessor.pkl')
model = joblib.load('credit_card_eligibility_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
        try:
    # Get JSON data from request
            data = request.json

    # convert JSON data to DataFrame
            input_features = pd.DataFrame(data, index=[0])

    # preprocess the input features
            preprocessed_data = preprocessor.transform(input_features)

    # Make predictions
            prediction = model.predict(preprocessed_data)

    #return the prediction as jSON
            result = {'prediction': int(prediction[0])}
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)