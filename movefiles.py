
import os
import shutil

# Specify the source and destination directories
source_dir = '/home/working/fiverdude1'
dest_dir = '/home/working/ImageViewerandDescriptionWriter'

# List the files to move
files_to_move = ['complete7.py', 'img2.png', 'img1.png', 'requirements.txt', 'README.md']

# Loop through the list of files and move them
for file in files_to_move:
    src_path = os.path.join(source_dir, file)
    dest_path = os.path.join(dest_dir, file)
    
    # Check if the file exists in the source folder before moving
    if os.path.isfile(src_path):
        shutil.move(src_path, dest_path)
        print(f'Successfully moved {file} to {dest_dir}')
    else:
        print(f'{file} does not exist in {source_dir}')
