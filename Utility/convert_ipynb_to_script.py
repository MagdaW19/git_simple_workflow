"""Script to convert ipynb notebooks to py scripts"""
import os
import json


def get_files_with_extension(extension='.ipynb'):
    """Get list of paths for files with given extension    """
    files_list = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                fullpath = os.path.join(root, file)
                files_list.append(fullpath)
    return files_list


def deduplicate_hash(markdown):
    """Deduplicate # symbol in markdown """
    return markdown.replace('#', '').replace('\n', '\n#')


def extract_cell_text(cell):
    """ Extract code from code cell """
    text = ''
    if cell["cell_type"] == "code":
        text += ''.join(cell["source"])
    elif cell["cell_type"] == "markdown":
        text += '#'
        text += deduplicate_hash(''.join(cell["source"]))
    return text


def format_cell(i, cell):
    """Format display of notebook cell"""
    return f'# In[{i+1}]:\n{extract_cell_text(cell)}'


def convert_ipynb_to_py(file_path):
    """ Convert ipynb content to py script"""
    with open(file_path, "r") as file:
        ipynb_data = json.load(file)
        enum_cells = enumerate(ipynb_data['cells'])
        formated_cells = [format_cell(i, cell) for i, cell in enum_cells]
        script = '\n\n\n'.join(formated_cells) + '\n'
        return script


def main():
    """Main function that runs converting ipynb to py"""
    for input_file_path in get_files_with_extension('.ipynb'):
        new_folder_path = input_file_path.replace('Notebook', 'Script')
        output_file_path = new_folder_path.replace('.ipynb', '.py')
        script = convert_ipynb_to_py(input_file_path)

        with open(output_file_path, 'w') as file:
            file.write(script)


if __name__ == '__main__':
    main()
