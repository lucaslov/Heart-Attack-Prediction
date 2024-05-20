from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession


def get_kedro_catalog(project_path):
    path = Path(project_path)
    metadata = bootstrap_project(path)

    with KedroSession.create(metadata.project_name, path) as session:
        context = session.load_context()
        return context.catalog

catalog = get_kedro_catalog('heart-attack-prediction')

def get_dataset(dataset_name: str):
    return catalog.load(dataset_name).to_dict(orient='records')
