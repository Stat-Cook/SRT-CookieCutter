import os
import re


def max_work_package(strings):
    pattern = re.compile(r"[0-9]+$")
    matches = [pattern.findall(string) for string in strings]

    if any([len(i) > 1 for i in matches]):
        raise "Too many matches - check folder names"

    numeric_strings = [match[0] for match in matches if len(match) > 0]
    numerics = [float(string) for string in numeric_strings]

    return max(numerics)


def _make_wp_folder(n=1, root=".", root_start=2, wp_start=1):

    _iter = range(n)

    for i in _iter:
        wp_prefix = int(root_start + i)
        wp_suffix = int(wp_start + i)
        wp_id = f"5.{wp_prefix}"

        wp_folder = f"{wp_id} WP{wp_suffix}"
        wp_path = os.path.join(root, wp_folder)
        os.makedirs(wp_path)

        instrument_folder = f"{wp_id}.1 Instruments"
        instrument_path = os.path.join(wp_path, instrument_folder)
        os.makedirs(instrument_path)

        raw_data_folder = f"{wp_id}.2 Raw Data"
        raw_data_path = os.path.join(wp_path, raw_data_folder)
        os.makedirs(raw_data_path)


def append_work_packages(n_to_add, wp_root="."):
    root_list = os.listdir(wp_root)
    paths = [os.path.join(wp_root, i) for i in root_list]
    is_directory = [os.path.isdir(i) for i in paths]

    prefix_start = sum(is_directory) + 1
    suffix_start = max_work_package(root_list) + 1

    _make_wp_folder(n_to_add, wp_root, prefix_start, suffix_start)

