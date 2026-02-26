import os

def write_file(working_directory, file_path, content):
    try:
        # absolute path of allowed working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # construct full path to target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # check if target_file is in within working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file])

        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # checking if parent directories exist, when True continue
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
            
        #open file in file_path and overwrite with content
        with open(target_file, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'            

    # catch unexpected system or permission errors
    except Exception as e:
        return f"Error: {str(e)}"