# imports
import os
import json

# define functions
def get_files_with_extension(extension='.ipynb'):
    """Get list of paths for files in current directory (recursively) with given extension    """
    files_list = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                fullpath = os.path.join(root, file)
                files_list.append(fullpath)
    return files_list

def clear_cell_ipynb(cell):
    """Modify cell metadata for ipynb cells"""
    cell["execution_count"]=None
    cell["outputs"]=[]
    return cell

def clear_notebook_metadata(file_path):
    """Clear metadata for ipynb file by overwriting it in place  """
    with open(file_path,"r") as f:
        data = json.load(f)
        data['cells'] = [clear_cell_ipynb(cell) for cell in data['cells']]
        json.dump(data, open(file_path, "w"), indent = 4)

# clear all ipynb files in place
for file in get_files_with_extension():
    clear_notebook_metadata(file)