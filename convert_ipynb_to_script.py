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

def extract_cell_text(cell):
    """ Extract code from code cell """
    text = ''
    if cell["cell_type"]=="code":
        text += ''.join(cell["source"])
    elif cell["cell_type"]=="markdown":
        text += ''.join(cell["source"])
    return text

def convert_ipynb_to_py(file_path, cell_info=False):
    """ Convert ipynb content to py script"""
    with open(file_path,"r") as f:
        ipynb_data = json.load(f)
        script = ''
        for cell in ipynb_data['cells']:
            script += extract_cell_text(cell) + '\n\n'
        return script
        
# export notebooks to scripts
def main():
    for input_file_path in get_files_with_extension('.ipynb'):

        output_file_path = input_file_path.replace('.ipynb','.py')
        script = convert_ipynb_to_py(input_file_path)

        with open(output_file_path,'w') as f:
            f.write(script)

if __name__ == '__main__':
    main()