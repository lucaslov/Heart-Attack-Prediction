from sklearn.neighbors import KNeighborsClassifier
from autogluon.tabular import TabularPredictor

# def train(heart_train_x, heart_train_y):
#     model_knn = KNeighborsClassifier(n_neighbors=9, leaf_size=20)
#     model_knn.fit(heart_train_x, heart_train_y.values.ravel())
#     return model_knn

def train(heart_train):
    predictor = TabularPredictor(label='output', eval_metric="accuracy").fit(heart_train, presets="good_quality")
    return predictor