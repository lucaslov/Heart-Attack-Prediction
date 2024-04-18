from kedro.pipeline import Pipeline, node, pipeline
from .nodes import age_distribution

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=age_distribution,
                inputs="heart",
                outputs=None,
                name="age_distribution_node"
            )
        ]
    )