from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split, split_test_output, split_train_output

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # node(
            #     func=split,
            #     inputs=['heart_processed','params:train_weight','params:validation_weight','params:test_weight'],
            #     outputs=['heart_train','heart_validation','heart_test'],
            #     name="split_node",
            # ),
            # node(
            #     func=split_train_output,
            #     inputs=['heart_train'],
            #     outputs=['heart_train_x','heart_train_y'],
            #     name="split_train_output_node",
            # ),
            # node(
            #     func=split_test_output,
            #     inputs=['heart_test'],
            #     outputs=['heart_test_x','heart_test_y'],
            #     name="split_test_output_node",
            # )
            node(
                func=split,
                inputs=['heart_processed'],
                outputs=['heart_train','heart_test'],
                name="split_node",
            )
        ]
    )