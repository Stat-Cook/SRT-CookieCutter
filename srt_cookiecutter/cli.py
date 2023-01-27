"""
Implementation of the csv_2_tsv CLI interface.
"""

import argparse

from srt_cookiecutter.cutter import cutter


def project_init():
    """
    CLI to the csv_2_tsv.spider function.
    Returns:
        int
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", help='Name for the project',
                        default="SRT Project", nargs="?", type=str)

    parser.add_argument("-pm", "--project_manager", help='Project manager details',
                        default="n/a", nargs="?", type=str)

    parser.add_argument("-pi", "--principal_investigator", help='Principal investigator details',
                        default="n/a", nargs="?", type=str)

    parser.add_argument("-wp", "--work_packages",
                        default="1", nargs="?", type=int,
                        help='')

    parser.add_argument("-co", "--content_only", action="store_true")

    args = parser.parse_args()

    val = cutter(args.project_name, args.project_manager,
                 args.principal_investigator, args.work_packages,
                 args.content_only)

    return val
