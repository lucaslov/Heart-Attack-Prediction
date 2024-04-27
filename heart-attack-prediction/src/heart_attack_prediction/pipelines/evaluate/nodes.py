import logging
from sklearn.metrics import accuracy_score, roc_auc_score
from autogluon.tabular import TabularPredictor
import wandb

# def evaluate(model_knn, heart_test_x, heart_test_y):   
#     y_pred = model_knn.predict(heart_test_x)
#     y_probas = model_knn.predict_proba(heart_test_x)[:,1]
    
#     accuracy = accuracy_score(heart_test_y, y_pred)
#     roc_auc = roc_auc_score(heart_test_y, y_probas)
#     print('ROC AUC: %.3f' % roc_auc)
#     print('Accuracy: %.3f' % accuracy)

#     # wandb.sklearn.plot_feature_importances(model_knn)
    
#     logger = logging.getLogger(__name__)
#     logger.info("Model has an accuracy of %.3f on test data.", accuracy)
#     logger.info("Model has an ROC AUC of %.3f on test data.", roc_auc)
    
#     wandb.log({'accuracy': accuracy, 'roc_auc': roc_auc})

def evaluate(predictor, heart_test):
    predictons = predictor.predict(heart_test)
    performance = predictor.evaluate(heart_test)

    wandb.log({'accuracy': performance["accuracy"], 'roc_auc': performance["roc_auc"]})