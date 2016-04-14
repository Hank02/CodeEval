import os
import sys

def get_filesize():
    in_file = sys.argv[1]
    file_data = os.stat(in_file)
    return file_data.st_size

if __name__ == "__main__":
    result = get_filesize()
    print(result)