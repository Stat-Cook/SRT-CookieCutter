"""
Implementation of the append workpackage CLI interface.
"""

import argparse

from srt_cookiecutter.append_work_packages import append_work_packages


def append_wp_cli():
    """
    CLI to the srt_cookiecutter.cutter function.
    Returns:
        int
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--n", help='Number of new work package folders to create',
                        default="1", nargs="?", type=int)

    parser.add_argument("-r", "--root", help='Root for the work packages folder',
                        default=".", nargs="?", type=str)

    args = parser.parse_args()

    val = append_work_packages(args.n, args.root)

    return val
