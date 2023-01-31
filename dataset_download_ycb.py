import os
from urllib.request import Request, urlopen



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

# Defining the files_to_download = ["berkeley_rgbd", "berkeley_rgb_highres", "berkeley_processed", "google_16k", "google_64k", "google_512k"]
files_to_download = ["google_64k"]

# Extract all files from the downloaded .tgz, and remove .tgz files.
# If false, will just download all .tgz files to output_directory
extract = True


# Defining the urls to download the files
base_url = "http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/data/"
objects_url = "https://ycb-benchmarks.s3.amazonaws.com/data/objects.json"

# Creating the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Defining a function to fetch the objects list from json file in the url
def fetch_objects(url):
    response = urlopen(url)
    print(response)
