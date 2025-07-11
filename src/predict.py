from DataCollector import get_live_traffic_data
from preprocess import build_pipeline
import pandas as pd
import joblib

def predict():
    data = get_live_traffic_data()

    pipeline = joblib.load('models/preprocess_pipeline.pkl')
    model = joblib.load('models/traffic_model.pkl')

    pred = model.predict(pipeline.transform(pd.DataFrame([data])))
    print(f"Predicted: {pred[0]}, Actual travel time: {data['travel_time_min']}")

    # Compare manually to Google Maps live info
    df = pd.DataFrame([data])
    X_live = pipeline.transform(df)
    prediction = model.predict(X_live)
    print(f"[{data['timestamp']}] Predicted Congestion Level: {prediction[0]}")

if __name__ == "__main__":
    predict()
