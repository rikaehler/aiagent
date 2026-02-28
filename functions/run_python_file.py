import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        # absolute path of allowed working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # construct full path to target file
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # check if target_file is in within working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, absolute_file_path])

        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not absolute_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]

        # add args to command if needed
        if args is not None:
            command.extend(args)
        
        # use subprocess.run() to run the command with necessary arguments
        # returns CompletedProcess object into 'process'
        process = subprocess.run(
                command,                    # the command
                cwd = working_dir_abs,      # current working directory
                capture_output = True,      # capture stdout and stderr
                text = True,                # decode output to stings, not bytes
                timeout = 30                # timeout in second to precent infinite execution
            )

        # create output string
        output_parts = []

        # check return code and add it
        if process.returncode != 0:
            output_parts.append(f"rocess exited with code {process.returncode}")
        
        # check stdout and stderr
        if not process.stdout and not process.stderr:
            output_parts.append("No output produced")
        else:
            if process.stdout:
                output_parts.append(f"STDOUT:\n{process.stdout.strip()}")
            if process.stderr:
                output_parts.append(f"STDERR:\n{process.stderr.strip()}")
        
        #join parts into single string
        return "\n".join(output_parts).strip()

    # catch unexpected system or permission errors
    except Exception as e:
        return f"Error: executing Python file {str(e)}"