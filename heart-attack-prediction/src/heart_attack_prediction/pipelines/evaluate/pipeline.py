"""
This is a boilerplate pipeline 'evaluate'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # node(
            #     func=evaluate,
            #     inputs=["model_knn", "heart_test_x", "heart_test_y"],
            #     outputs=None,
            #     name="evaluate_node",
            # ),
            node(
                func=evaluate,
                inputs=["preditor", "heart_test"],
                outputs=None,
                name="evaluate_node",
            ),
        ]
    )
