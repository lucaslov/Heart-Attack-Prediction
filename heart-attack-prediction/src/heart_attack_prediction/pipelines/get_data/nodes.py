import pandas as pd
import requests
from io import BytesIO

def get_heart(heart_url):
    response = requests.get(heart_url).content
    return pd.read_csv(BytesIO(response))