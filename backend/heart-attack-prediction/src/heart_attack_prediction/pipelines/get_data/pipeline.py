from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_heart

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_heart,
                inputs="params:heart_url",
                outputs="heart",
                name="get_heart_node",
            )
        ]
    )
