
def heart_preprocess(heart):
    heart.fillna(method='ffill', inplace=True)
    heart.dropna(inplace=True)


    return heart
