from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train,
                inputs=dict(
                    heart_train='heart_train',
                    label='params:label',
                    eval_metric='params:eval_metric',
                    path='params:path',
                    presets='params:presets',
                ),
                outputs='predictor',
                name="train_node",
            )
        ]
    )