import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# List of folders to ignore
IGNORE_FOLDERS = ["__pycache__", "static", "sound", "instance", "logs", "migration", "obj"]

# Function to read all files in a directory and annotate with titles and subtitles, ignoring specified folders
def read_and_annotate_codebase(directory):
    code = ""
    toc = "Table of Contents:\n\n"
    for root, dirs, files in os.walk(directory):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
        folder = os.path.relpath(root, directory)
        if folder == ".":
            folder = "Root"
        code += f"# Folder: {folder}\n"
        toc += f"- {folder}/\n"
        for file in files:
            if file.endswith('.py') or file == 'README.md':  # Adjust file types as needed
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_content = f.read()
                code += f"## File: {file}\n"
                toc += f"  - {file}\n"
                code += file_content + "\n"
    return code, toc

# Function to select a directory
def select_directory():
    root = Tk()
    root.withdraw()  # Hide the root window
    directory = askdirectory()  # Open a dialog to ask for directory
    return directory

# Select the directory
selected_directory = select_directory()
if not selected_directory:
    print("No directory selected. Exiting...")
else:
    # Read and annotate the codebase
    codebase, toc = read_and_annotate_codebase(selected_directory)
    codebase_with_toc = codebase + "\n\n" + toc

    # Save the annotated codebase to a new file
    output_file_path = os.path.join(selected_directory, "annotated_codebase_with_toc.txt")
    with open(output_file_path, "w") as f:
        f.write(codebase_with_toc)

    print(f"Annotated codebase with TOC has been saved to '{output_file_path}'.")
