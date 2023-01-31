import os



# Defining folder for downloading the dataset
output_directory = os.path.join("models", "ycb")


# Defining the list ob object to download from 
# http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/
# by selecting "all" all the files will be downloaded
# or you can selct a list of objects
objects_to_download = "all"
# objects_to_download = ["001_chips_can", 
#                        "002_master_chef_can",
#                        "003_cracker_box",
#                        "004_sugar_box"]