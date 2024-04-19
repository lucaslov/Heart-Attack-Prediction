"""
This is a boilerplate pipeline 'preprocess'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import heart_preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=heart_preprocess,
                inputs=['heart'],
                outputs='heart_processed',
                name="heart_preprocess_node",
            ),
        ]
    )
