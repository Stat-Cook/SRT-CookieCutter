from importlib import resources
import os
from distutils.dir_util import copy_tree
from shutil import rmtree
from cookiecutter.main import cookiecutter


def cutter(project_name="SRT Project", project_manager="n/a",
           principal_investigator="n/a", work_packages=1,
           content_only=False):

    output_dir = "."
    temp_root = "_Temp"

    with resources.path(__package__, '__init__.py') as p:
        init_loc = p
    folder, _ = os.path.split(init_loc)

    if content_only:
        os.mkdir(temp_root)
        output_dir = os.path.join(output_dir, temp_root)

    extra_context = {
        "project_name": project_name,
        "PM": project_manager,
        "PI": principal_investigator,
        "WP": work_packages
    }

    val = cookiecutter(folder, no_input=True, overwrite_if_exists=False,
                       extra_context=extra_context, output_dir=output_dir)

    if content_only:

        from_dir = os.path.join(temp_root, project_name)
        to_dir = "."
        copy_tree(from_dir, to_dir)
        rmtree(temp_root)

    return val
