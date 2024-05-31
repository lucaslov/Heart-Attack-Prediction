from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from models.model import HeartDataSet, HeartPrediction
from services.kedro import get_dataset, run_pipeline
from services.prediction import get_prediction
import pandas as pd
import os

router = APIRouter()

@router.get("/heart_data/{dataset_name}", response_model=List[HeartDataSet])
async def get_heart_data(dataset_name: str):
    return get_dataset(dataset_name)

@router.post("/predict", response_model=int)
async def predict(data: HeartPrediction):
    return get_prediction(data)

@router.post("/import_data")
async def import_data(file: UploadFile = File(...)):
    try:
        file_location = f"data/01_raw/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        
        df = pd.read_csv(file_location)
        
        run_pipeline()
        
        return {"message": "Dataset imported and pipeline executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
