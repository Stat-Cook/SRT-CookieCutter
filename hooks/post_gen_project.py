import os
import sys
from shutil import rmtree

try:
    import analysis_cli
except ModuleNotFoundError:
    repo_address = "https://github.com/Stat-Cook/Analysis-CookieCutter"
    raise(ModuleNotFoundError(
        f"Module 'analysis_cli' not found \n run 'pip install git+{repo_address}' to install. ")
    )

try:
    import docx
except ModuleNotFoundError:
    raise(ModuleNotFoundError(
        f"Module 'docx' not found \n run 'pip install python-docx' to install. ")
    )

# Set up project to read
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
sys.path.insert(0, PROJECT_DIRECTORY)  # add the working directory to the path
from hook_modules import DirMaker, DocReplacer, remove_files

# Assign useful variables
WP_n = {{cookiecutter.WP}}
project_name = '{{cookiecutter.project_name}}'

wp_f = lambda i: f"5.{i+2} WP{i+1}"

# Make data folder tree
data_root = DirMaker("5. Anonymised Data (No PID)", "5")
data_root.make_child("Resources")

for i in range(WP_n):
    wp_root = data_root.make_child(f"WP{i+1}")

    wp_root.make_children(["Instruments", "Raw Data"])

    analysis_root = os.path.join(PROJECT_DIRECTORY, wp_root.parent)
    analysis_cli.cutter(i+1, 1, analysis_root)

# Replace occurrences of key words in word docs
dr = DocReplacer(".")
dr()

# Remove vestigial files
rmtree("hook_modules")
remove_files(".")
