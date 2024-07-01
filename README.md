Here is a README file that explains the two scripts, their purpose, and includes an MIT license:

---

# Python Project Compilation Scripts

## Overview
These scripts are designed to compile a Python project into a single annotated file. This makes it easier to upload the project to an LLM (Language Model) like ChatGPT or others for processing or analysis.

## Scripts

### 1. Annotate Codebase without Tokenization

#### File: `annotate_codebase.py`

This script reads all `.py` and `README.md` files from the selected directory, annotates them with folder and file headers, and compiles them into a single file with a table of contents.

#### How to Use:
1. Run the script.
2. Select the directory containing the Python project.
3. The script will generate an `annotated_codebase_with_toc.txt` file in the selected directory.

#### Example Usage:
```python
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
```

### 2. Annotate and Tokenize Codebase

#### File: `annotate_and_tokenize_codebase.py`

This script performs the same annotation as the first script but also tokenizes the annotated codebase using the `t5-small` model from Hugging Face's Transformers library. It saves both the annotated codebase and the tokenized data to separate files.

#### How to Use:
1. Run the script.
2. Select the directory containing the Python project.
3. The script will generate `annotated_codebase_with_toc.txt` and `tokenized_codebase.json` files in the selected directory.

#### Example Usage:
```python
import os
import json
from tkinter import Tk
from tkinter.filedialog import askdirectory
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

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

    # Tokenize the codebase with TOC
    inputs = tokenizer(codebase_with_toc, return_tensors="pt", truncation=True, padding="longest", max_length=512)

    # Save tokenized inputs to files
    tokenized_output_path = os.path.join(selected_directory, "tokenized_codebase.json")
    with open(tokenized_output_path, "w") as f:
        json.dump({
            "input_ids": inputs["input_ids"].tolist(),
            "attention_mask": inputs["attention_mask"].tolist()
        }, f, indent=4)

    print(f"Annotated codebase with TOC has been saved to '{output_file_path}'.")
    print(f"Tokenized version has been saved to '{tokenized_output_path}'.")
    print("Tokenization completed.")
```

## License

MIT License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Author
Made by Kim Garrick
