from kedro.pipeline import Pipeline, node, pipeline
from .nodes import plot

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=plot,
                inputs="heart",
                outputs=None,
                name="plots_node"
            )
        ]
    )