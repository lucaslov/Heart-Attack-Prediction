from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularDataset

def split(heart):
    train_data, test_data = train_test_split(heart, test_size=0.2, random_state=42)
    train_data = TabularDataset(train_data)
    test_data = TabularDataset(test_data)

    return train_data, test_data