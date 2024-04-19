from sklearn.neighbors import KNeighborsClassifier

def train(heart_train_x, heart_train_y):
    model_knn = KNeighborsClassifier(n_neighbors=9, leaf_size=20)
    model_knn.fit(heart_train_x, heart_train_y)
    return model_knn
