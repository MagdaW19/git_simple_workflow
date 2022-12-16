"""Script that cleans ipynb files from metadata"""


import json
from find_files import get_files_with_extension


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
