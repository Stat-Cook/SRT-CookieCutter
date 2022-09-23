import os
import sys
from shutil import rmtree

import analysis_cli

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
sys.path.insert(0, PROJECT_DIRECTORY)  # add the working directory to the path
from hook_modules import DirMaker, DocReplacer

WP_n = {{cookiecutter.WP}}
project_name = '{{cookiecutter.project_name}}'

wp_f = lambda i: f"5.{i+2} WP{i+1}"

data_root = DirMaker("5. Anonymised Data (No PID)", "5")
data_root.make_child("Resources")

for i in range(WP_n):
    wp_root = data_root.make_child(f"WP{i+1}")

    wp_root.make_children(["Instruments", "Raw Data"])

    analysis_root = os.path.join(PROJECT_DIRECTORY, wp_root.parent)
    analysis_cli.cutter(i+1, 1, analysis_root)


print(PROJECT_DIRECTORY)

dr = DocReplacer(".")
dr()

rmtree("hook_modules")
