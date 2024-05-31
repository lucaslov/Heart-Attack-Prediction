import os
import pandas as pd
from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from kedro.runner import SequentialRunner
from fastapi import HTTPException

def get_kedro_context(project_path):
    path = Path(project_path)
    metadata = bootstrap_project(path)

    with KedroSession.create(metadata.project_name, path) as session:
        context = session.load_context()
        return context

context = get_kedro_context('heart-attack-prediction')
catalog = context.catalog

def get_dataset(dataset_name: str):
    return catalog.load(dataset_name).to_dict(orient='records')

def run_pipeline():
    try:
        runner = SequentialRunner()
        context.run(runner=runner)
    except AttributeError:
        raise HTTPException(status_code=500, detail=f"'KedroContext' object has no attribute 'run'")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run pipeline: {e}")

def delete_dataset(dataset_name: str):
    try:
        catalog.save(dataset_name, pd.DataFrame())  # Save an empty DataFrame to clear the table
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete dataset: {e}")

def add_row_to_dataset(dataset_name: str, row: dict):
    try:
        df = catalog.load(dataset_name)
        new_row_df = pd.DataFrame([row])
        updated_df = pd.concat([df, new_row_df], ignore_index=True)
        catalog.save(dataset_name, updated_df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add row: {e}")

def remove_row_from_dataset(dataset_name: str, row_id: int):
    try:
        df = catalog.load(dataset_name)
        if row_id < 0 or row_id >= len(df):
            raise HTTPException(status_code=400, detail="Invalid row ID")
        df = df.drop(row_id).reset_index(drop=True)
        catalog.save(dataset_name, df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to remove row: {e}")

def append_data_to_dataset(dataset_name: str, file_location: str):
    try:
        with open(file_location, "r") as f:
            content = f.read()
            print("File Content:\n", content)
        
        new_data = pd.read_csv(file_location)
        print("New Data:\n", new_data.head())  

        if new_data.empty or new_data.columns.size == 0:
            raise HTTPException(status_code=400, detail="Uploaded CSV is empty or invalid")

        existing_data = catalog.load(dataset_name)
        print("Existing Data:\n", existing_data.head())  

        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        print("Combined Data:\n", combined_data.head())

        catalog.save(dataset_name, combined_data)
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="No columns to parse from file")
    except pd.errors.ParserError as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV file: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to append data: {e}")

