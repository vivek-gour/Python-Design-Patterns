import zipfile
import shutil
import os

years = ['2020', '2021']

# Specify the path where you want to extract the contents of the zip file
files_dir = 'E:/Download_Folder/zomato'

# Specify the path to the archive folder
archive_folder = 'archive'
for year in years:
    for zipped_file_name in os.listdir(os.path.join(files_dir, year)):
        zipped_file_path = os.path.join(files_dir, year, zipped_file_name)
        # Open the zip file
        with zipfile.ZipFile(zipped_file_path, 'r') as zip_file:
            # Extract all contents of the zip file to the specified folder
            zip_file.extractall(os.path.join(files_dir, year))

        archive_folder_path = os.path.join(files_dir, archive_folder, year, zipped_file_name)
        # Move the original .zip file to the archive folder
        shutil.move(zipped_file_path, archive_folder_path)

