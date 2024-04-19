from sklearn.model_selection import train_test_split

def split(heart, train_weight, validation_weight, test_weight):
    total_weight = train_weight + validation_weight + test_weight
    
    # Calculate proportions
    train_size = train_weight / total_weight
    validation_size = validation_weight / total_weight
    test_size = test_weight / total_weight
    
    # Split the data
    train_data, remaining_data = train_test_split(heart, train_size=train_size, random_state=42)
    validation_data, test_data = train_test_split(remaining_data, train_size=validation_size/(validation_size + test_size), random_state=42)
    
    return train_data, validation_data, test_data

def split_output(heart_train):
    heart_train_x = heart_train.drop(columns=['target'])
    heart_train_y = heart_train['target']
    
    return heart_train_x, heart_train_y