"""Module with function for finding files"""


import os


def get_files_with_extension(extension='.ipynb',directory='.'):
    """Get list of paths for files with given extension """
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                fullpath = os.path.join(root, file)
                files_list.append(fullpath)
    return files_list
