import os
import shutil
import sys

def extract_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # Rename file if it already exists in the destination directory
            counter = 1
            file_name, file_extension = os.path.splitext(dest_file)
            while os.path.exists(dest_file):
                dest_file = f"{file_name}_{counter}{file_extension}"
                counter += 1

            try:
                shutil.copy(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")
            except Exception as e:
                print(f"Error copying {src_file} to {dest_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_files.py [source directory] [destination directory]")
        sys.exit(1)

    print("Started")
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    extract_files(source_directory, destination_directory)
