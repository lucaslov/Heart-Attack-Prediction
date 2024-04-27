from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor, TabularDataset

# def split(heart, train_weight, validation_weight, test_weight):
#     total_weight = train_weight + validation_weight + test_weight
    
#     # Calculate proportions
#     train_size = train_weight / total_weight
#     validation_size = validation_weight / total_weight
#     test_size = test_weight / total_weight
    
#     # Split the data
#     train_data, remaining_data = train_test_split(heart, train_size=train_size, random_state=42)
#     validation_data, test_data = train_test_split(remaining_data, train_size=validation_size/(validation_size + test_size), random_state=42)
    
#     return train_data, validation_data, test_data

# def split_train_output(heart_train):
#     return heart_train.drop(columns=['output']), heart_train['output']

# def split_test_output(heart_test):
#     return heart_test.drop(columns=['output']), heart_test['output']

def split(heart):
    train_data, test_data = train_test_split(heart, test_size=0.2, random_state=42)
    train_data = TabularDataset(train_data)
    test_data = TabularDataset(test_data)

    return train_data, test_data