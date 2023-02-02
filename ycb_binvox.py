import os
import dataset_download_ycb
import shutil

# Defining folder for downloading the dataset
output_directory = os.path.join("models", "binvox_files")

# Creating the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def obj2binvox(input_path, file_name, ext, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    command = "./binvox -d 256 " + input_path + file_name + ext
    print(command)
    print("converting" + input_path + "to" + output_path + file_name)
    if (os.system(command) ==0):
        shutil.move(input_path + file_name + ".binvox", output_path)


# specify the directory containing the folders
root_dir = "models/ycb/"

# loop through each folder in the directory
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    for root, dirs,files in os.walk(folder_path):
        for file in files:
            if file.endswith(".obj"): 
                file_name, ext = os.path.splitext(file)  
                output_folder_path = os.path.join(output_directory,folder_name)
                obj2binvox(folder_path + "/google_64k/", file_name, ext, output_folder_path)
   