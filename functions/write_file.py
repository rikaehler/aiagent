import os
from google.genai import types # type: ignore

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
    

# building a schema for function write_file() - tells LLM how the function should be called
schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "Writes text content to a specified file path, creating the file if it doesn't exist or overwriting it if it does.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path to the file where content should be written, relative to the working directory.",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "The text content to write into the file.",
            ),
        },
        required = ["file_path", "content"], # both are strictly necessary to perform a write operation
    ),
)