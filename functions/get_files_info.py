import os

def get_files_info(working_directory, directory="."):
    try:
        # absolute path of allowed working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # construct full path to target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # check if target_file is in within working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])

        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # iterate over items in target directory and record info to create return string with it
        items_info = []

        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            items_info.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(items_info)        
    
    # catch unexpected system or permission errors
    except Exception as e:
        return f"Error: {str(e)}"