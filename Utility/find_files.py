"""Module with function for finding files"""


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

