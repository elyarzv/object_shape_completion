# object_shape_completion
My goal in this repository is to train a network to complete the shape of an object with a single shot RGB-D image.

Later on this repository will be used to grasp the object and another network will use the output of this repository to generate highly accurate grasp samples.

## Downloading YCB data
The dataset_download_ycb.py file is created to download the dataset.
There are some options but for this repo the default options are applied to download the 3D models.
The files will be stored in model/ycb folder.

## Converting 3D models to binvox files
The ycb_binvox.py script converts downloaded models to .binvox files.
The converted files will be stored in corresponding folder inside models/binvox_files folder.

### Viewing binvox files
The created binvox files can be viewed by the viewvox execution file. 
For example to view the binvox file /models/binvox_files/002_master_chef_can/textured.binvox the following command should be run:

`./viewvox /models/binvox_files/002_master_chef_can/textured.binvox `