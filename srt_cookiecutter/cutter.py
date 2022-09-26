from importlib import resources
import os
from cookiecutter.main import cookiecutter


def cutter(project_name="SRT Project", project_manager="n/a",
           principal_investigator="n/a", work_packages=1):
    
    with resources.path(__package__, '__init__.py') as p:
        init_loc = p
    folder, _ = os.path.split(init_loc)

    extra_context = {
        "project_name": project_name,
        "PM": project_manager,
        "PI": principal_investigator,
        "WP": work_packages
    }

    val = cookiecutter(folder, no_input=True, overwrite_if_exists=True,
                       extra_context=extra_context)

    return val
