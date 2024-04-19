from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split,
                inputs=['heart','params:train_weight','params:validation_weight','params:test_weight'],
                outputs=['heart_train','heart_validation','heart_test'],
                name="split_node",
            )
        ]
    )