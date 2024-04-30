from fastapi import APIRouter
from typing import List
from model import HeartDataSet, HeartPrediction
from services.kedro import get_dataset
from services.prediction import get_prediction

router = APIRouter()

@router.get("/heart_data/{dataset_name}", response_model=List[HeartDataSet])
async def get_heart_data(dataset_name: str):
    return get_dataset(dataset_name)

@router.post("/predict", response_model=int)
async def predict(data: HeartPrediction):
    return get_prediction(data)
