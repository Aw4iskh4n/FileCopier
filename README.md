# FileCopier

FileCopier is a simple Python utility for copying files from a source directory to a destination directory. It handles files in nested subdirectories and ensures that no files are overwritten in the destination directory. If a file with the same name already exists, FileCopier renames the new file to maintain uniqueness.

## Installation

To use FileCopier, ensure Python is installed on your system. If Python is not installed, download it from the [Python official website](https://www.python.org/downloads/).

### Cloning the Repository

Clone the FileCopier repository to your local machine using Git:

```bash
git clone https://github.com/your-username/FileCopier.git
```
```
cd FileCopier
```

Replace `your-username` with your GitHub username.

## Usage

Navigate to the cloned directory in your command line or terminal and run:

\```bash
python extract_files.py [source_directory] [destination_directory]
\```

Replace `[source_directory]` with the path of the directory from which you want to copy files, and `[destination_directory]` with the path of the directory where you want the files copied.

### Example

\```bash
python extract_files.py "C:\\Users\\Example\\Downloads\\SourceFolder" "C:\\Users\\Example\\Documents\\DestinationFolder"
\```

## Features

- Copies all files from the specified source directory to the destination directory.
- Preserves file names and ensures no file overwriting in the destination directory.
- Renames incoming files if a file with the same name exists in the destination.

## Contributing

Contributions to FileCopier are welcome. Please ensure your code adheres to the project's standards and include tests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
