import os
from urllib.request import Request, urlopen
import json
import urllib
import sys



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
    html = response.read()
    objects = json.loads(html)
    return objects["objects"]


def download_file(url, filename):
    """ Downloads files from a given URL """
    u = urlopen(url)
    f = open(filename,"wb")
    file_size = int(u.getheader("Content-Length"))    
    print("Downloading: {} ({} MB)".format(filename, file_size/1000000.0))

    file_size_dl = 0
    block_sz = 65536
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl/1000000.0, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)
    f.close()

    def tgz_url(object, type):
    """ Get the TGZ file URL for a particular object and dataset type """
    if type in ["berkeley_rgbd", "berkeley_rgb_highres"]:
        return base_url + "berkeley/{object}/{object}_{type}.tgz".format(object=object,type=type)
    elif type in ["berkeley_processed"]:
        return base_url + "berkeley/{object}/{object}_berkeley_meshes.tgz".format(object=object,type=type)
    else:
        return base_url + "google/{object}_{type}.tgz".format(object=object,type=type)

    def extract_tgz(filename, dir):
    """ Extract a TGZ file """
    tar_command = "tar -xzf {filename} -C {dir}".format(filename=filename,dir=dir)
    os.system(tar_command)
    os.remove(filename)

    def check_url(url):
    """ Check the validity of a URL """
    try:
        request = Request(url)
        request.get_method = lambda : 'HEAD'
        response = urlopen(request)
        return True
    except Exception as e:
        return False


if __name__ == "__main__":

    # Grab all the object information
    objects = fetch_objects(objects_url)

    # Download each object for all objects and types specified
    for object in objects:
        if objects_to_download == "all" or object in objects_to_download:
            for file_type in files_to_download:
                url = tgz_url(object, file_type)
                if not check_url(url):
                    continue
                filename = "{path}/{object}_{file_type}.tgz".format(
                    path=output_directory,
                    object=object,
                    file_type=file_type)
                download_file(url, filename)
                if extract:
                    extract_tgz(filename, output_directory)
