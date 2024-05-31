from http.client import HTTPException
from models.model import HeartPrediction
import pandas as pd
from autogluon.tabular import TabularPredictor

def get_prediction(data: HeartPrediction):
    predictor = TabularPredictor.load('heart-attack-prediction/AutogluonModels/')
    try:
        data_df = pd.DataFrame([data.dict()])
        prediction = predictor.predict(data_df)
        return prediction.iloc[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))