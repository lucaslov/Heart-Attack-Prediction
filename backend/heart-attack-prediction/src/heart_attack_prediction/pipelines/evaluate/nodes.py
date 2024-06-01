import wandb

def evaluate(predictor, heart_test):
    predictons = predictor.predict(heart_test)
    performance = predictor.evaluate(heart_test)

    wandb.log({'accuracy': performance["accuracy"], 'roc_auc': performance["roc_auc"]})