import os
from config import *

def get_file_content(working_directory, file_path):
    try:
        # absolute path of allowed working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # construct full path to target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # check if target_file is in within working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file])

        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # open target_file and read MAX_CHARS
        with open(target_file, 'r', encoding='utf-8') as file:
            file_content_string = file.read(MAX_CHARS)
            
            # check if end-of-file or MAX_CHARS by reading one more character
            if file.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return file_content_string

    # catch unexpected system or permission errors
    except Exception as e:
        return f"Error: {str(e)}"