from kedro.framework.hooks import hook_impl
from kedro.framework.startup import ProjectHooks
from dotenv import load_dotenv
import os

class ProjectHooks(ProjectHooks):

    @hook_impl
    def before_pipeline_run(self, *args, **kwargs):
        print('Running')
        load_dotenv() 

