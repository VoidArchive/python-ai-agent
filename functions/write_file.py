import os


def write_file(working_directory, file_path, content):
    try:
        # Get absolute paths
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file is within working directory
        if not file_path_abs.startswith(working_dir_abs):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create directory if it doesn't exist
        dir_path = os.path.dirname(file_path_abs)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Write content to file
        with open(file_path_abs, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"

