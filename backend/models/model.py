from typing import Optional
from pydantic import BaseModel

class HeartDataSet(BaseModel):
    age: Optional[int]
    sex: Optional[int]
    cp: Optional[int]
    trtbps: Optional[int]
    chol: Optional[int]
    fbs: Optional[int]
    restecg: Optional[int]
    thalachh: Optional[int]
    exng: Optional[int]
    oldpeak: Optional[float]
    slp: Optional[int]
    caa: Optional[int]
    thall: Optional[int]
    output: Optional[int]

class HeartPrediction(BaseModel):
    age: Optional[int]
    sex: Optional[int]
    cp: Optional[int]
    trtbps: Optional[int]
    chol: Optional[int]
    fbs: Optional[int]
    restecg: Optional[int]
    thalachh: Optional[int]
    exng: Optional[int]
    oldpeak: Optional[float]
    slp: Optional[int]
    caa: Optional[int]
    thall: Optional[int]
