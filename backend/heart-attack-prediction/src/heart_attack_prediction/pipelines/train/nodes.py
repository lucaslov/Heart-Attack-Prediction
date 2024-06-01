from autogluon.tabular import TabularPredictor

def train(heart_train):
    predictor = TabularPredictor(label='output', eval_metric="accuracy", path="heart-attack-prediction/AutogluonModels").fit(heart_train, presets="good_quality")
    return predictor