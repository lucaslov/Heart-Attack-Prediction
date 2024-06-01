
from autogluon.tabular import TabularPredictor

# def train(heart_train):
#     predictor = TabularPredictor(label='output', eval_metric="accuracy", path="AutogluonModels").fit(heart_train, presets="good_quality")
#     return predictor

def train(heart_train, label, eval_metric, path, presets):
    predictor = TabularPredictor(
        label=label,
        eval_metric=eval_metric,
        path=path
        ).fit(heart_train, presets=presets)
    return predictor