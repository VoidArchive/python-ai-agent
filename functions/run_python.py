import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        # Get absolute paths
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Check if file is within working directory
        if not file_path_abs.startswith(working_dir_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if file exists
        if not os.path.exists(file_path_abs):
            return f'Error: File "{file_path}" not found.'
        
        # Check if file is a Python file
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Execute the Python file
        result = subprocess.run(
            ['python', file_path_abs],
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Format the output
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
        
    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"