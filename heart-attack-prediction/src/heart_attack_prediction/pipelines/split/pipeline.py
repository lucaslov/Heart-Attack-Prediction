from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split, split_output

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split,
                inputs=['heart','params:train_weight','params:validation_weight','params:test_weight'],
                outputs=['heart_train','heart_validation','heart_test'],
                name="split_node",
            ),
            node(
                func=split_output,
                inputs=['heart_train'],
                outputs=['heart_train_x','heart_train_y'],
                name="split_output_node",
            )
        ]
    )