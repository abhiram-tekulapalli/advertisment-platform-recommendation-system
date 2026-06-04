from flask import Flask, request, jsonify
from flask_cors import CORS

import joblib
import pandas as pd


app = Flask(__name__)
CORS(app)

rf_model = joblib.load("model/random_forest_model.pkl")
feature_encoders = joblib.load("model/feature_encoders.pkl")
target_encoder = joblib.load("model/target_encoder.pkl")


def map_age_to_group(age):
    if 18 <= age < 25:
        return "18-25"
    elif 25 <= age < 35:
        return "25-35"
    elif 35 <= age < 45:
        return "35-45"
    elif 45 <= age <= 60:
        return "45-60"
    else:
        raise ValueError("Age out of range")


def map_price_to_category(price):
    if 1 <= price <= 9:
        return "1-9"
    elif 10 <= price <= 99:
        return "10-99"
    elif 100 <= price <= 999:
        return "100-999"
    elif 1000 <= price <= 9999:
        return "1000-9999"
    elif 10000 <= price <= 99999:
        return "10000-99999"
    else:
        raise ValueError("Price out of range")


def map_budget_to_category(budget):
    if 100 <= budget <= 999:
        return "100-999"
    elif 1000 <= budget <= 9999:
        return "1000-9999"
    elif 10000 <= budget <= 99999:
        return "10000-99999"
    elif 100000 <= budget <= 999999:
        return "100000-999999"
    else:
        raise ValueError("Budget out of range")


@app.route("/")
def home():
    return "Backend with ML model loaded successfully!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if data["product_category"] == "Skin Care":
        data["product_category"] = "Skincare"

    if data["product_category"] == "Apps and Websites":
        data["product_category"] = "App & Websites"
    try:

        product_category = data["product_category"]
        age = int(data["age"])
        target_geography = data["target_geography"]
        brand_awareness = data["brand_awareness"]
        price = int(data["price"])
        budget = int(data["budget"])

        age_group = map_age_to_group(age)
        price_category = map_price_to_category(price)
        budget_category = map_budget_to_category(budget)

        input_df = pd.DataFrame(
            [
                {
                    "product_category": product_category,
                    "target_age_group": age_group,
                    "target_geography": target_geography,
                    "brand_awareness": brand_awareness,
                    "price_category": price_category,
                    "budget_category": budget_category,
                }
            ]
        )

        for col in input_df.columns:
            input_df[col] = feature_encoders[col].transform(input_df[col])

        pred_encoded = rf_model.predict(input_df)
        pred_label = target_encoder.inverse_transform(pred_encoded)[0]

        return jsonify(
            {
                "recommended_platform": (
                    pred_label if pred_label else "No suitable platform found"
                )
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
