from fastapi import APIRouter, UploadFile, File, HTTPException, Body
from typing import List
from models.model import HeartDataSet, HeartPrediction
from services.kedro import add_row_to_dataset, append_data_to_dataset, delete_dataset, get_dataset, remove_row_from_dataset, run_pipeline
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

@router.delete("/delete_dataset/{dataset_name}")
async def delete_dataset_endpoint(dataset_name: str):
    try:
        delete_dataset(dataset_name)
        return {"message": f"Dataset {dataset_name} deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_row/{dataset_name}")
async def add_row_to_dataset_endpoint(dataset_name: str, row: dict):
    try:
        add_row_to_dataset(dataset_name, row)
        return {"message": f"Row added to dataset {dataset_name} successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/remove_row/{dataset_name}/{row_id}")
async def remove_row_from_dataset_endpoint(dataset_name: str, row_id: int):
    try:
        remove_row_from_dataset(dataset_name, row_id)
        return {"message": f"Row {row_id} removed from dataset {dataset_name} successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/run_pipelines")
async def run_pipelines_endpoint():
    try:
        run_pipeline()
        return {"message": "Pipelines executed and new model generated successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/import_data/{dataset_name}")
async def import_data_endpoint(dataset_name: str, file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        
        if not file_content:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        
        file_location = f"heart-attack-prediction/data/01_raw/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as file_object:
            file_object.write(file_content)
        
        if not os.path.exists(file_location) or os.path.getsize(file_location) == 0:
            raise HTTPException(status_code=400, detail="Failed to save uploaded CSV or file is empty")
        
        with open(file_location, "r") as file_check:
            saved_file_content = file_check.read()

        append_data_to_dataset(dataset_name, file_location)
        return {"message": f"Data appended to dataset {dataset_name} successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


