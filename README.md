# goit-pythonweb-hw-04
Homework 4: Asynchronous programming with Python. Course Fullstack Web Development with Python

## Async Folder Copy

This project uses Python's `asyncio` framework for asynchronous file operations. 
Files are recursively copied from a source folder to a target folder, organized by file extension.

### Features
- Recursively reads all files in a source folder.
- Copies files to a target folder, organized by file extension.
- Uses `aiopath` and `aioshutil` for asynchronous file system operations.

### Usage
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

To run the script, you can use the following command:
```bash
python main.py --source "/path/to/source" --target "/path/to/target"
```

