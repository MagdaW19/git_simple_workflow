"""Script that cleans ipynb files from metadata"""

import os
import json


def get_files_with_extension(extension='.ipynb'):
    """Get list of paths for files with given extension """
    files_list = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                fullpath = os.path.join(root, file)
                files_list.append(fullpath)
    return files_list


def clear_cell_ipynb(cell):
    """Modify cell metadata for ipynb cells"""
    cell["execution_count"] = None
    cell["outputs"] = []
    return cell


def clear_notebook_metadata(file_path):
    """Clear metadata for ipynb file by overwriting it in place  """
    with open(file_path, "r") as file:
        data = json.load(file)
        data['cells'] = [clear_cell_ipynb(cell) for cell in data['cells']]
        data['metadata'] = {}
        json.dump(data, open(file_path, "w"), indent=4)


def main():
    """Clear ipynb files from metadata """
    for file in get_files_with_extension():
        clear_notebook_metadata(file)


if __name__ == '__main__':
    main()
