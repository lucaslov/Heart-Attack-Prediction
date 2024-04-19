
import pandas


def heart_preprocess(heart) -> pandas.CSVDataset:
    heart.fillna(method='ffill', inplace=True)
    heart.dropna(inplace=True)
        

    return heart
