from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # node(
            #     func=train,
            #     inputs=['heart_train_x', 'heart_train_y'],
            #     outputs='model_knn',
            #     name="train_node",
            # )
            node(
                func=train,
                inputs=['heart_train'],
                outputs='predictor',
                name="train_node",
            )
        ]
    )