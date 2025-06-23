import os


def get_file_content(working_directory, file_path):
    try:
        # Get absolute paths
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file is within working directory
        if not file_path_abs.startswith(working_dir_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if file exists and is a regular file
        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file content with truncation at 10000 characters
        MAX_CHARS = 10000
        with open(file_path_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        # Check if file was truncated
        if len(file_content_string) == MAX_CHARS:
            # Check if there's more content by trying to read one more character
            with open(file_path_abs, "r") as f:
                f.read(MAX_CHARS)
                next_char = f.read(1)
                if next_char:  # If there's more content
                    file_content_string += (
                        f'\n[...File "{file_path}" truncated at 10000 characters]'
                    )

        return file_content_string

    except Exception as e:
        return f"Error: {str(e)}"
