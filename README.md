# object_shape_completion
This repository aims to train a neural network to complete the shape of objects using a single shot RGB-D image. The ultimate goal is to use the output of this network as input for another network, which will generate highly accurate grasp samples for grasping the objects.

## Downloading YCB data
The dataset_download_ycb.py file is created to download the dataset.
There are some options but for this repo the default options are applied to download the 3D models.
The files will be stored in model/ycb folder.

## Converting 3D models to [binvox][def] files
The ycb_binvox.py script converts downloaded models to .binvox files.
The converted files will be stored in corresponding folder inside models/binvox_files folder.

### Viewing binvox files
The created binvox files can be viewed by the [viewvox][def2] execution file. 
For example to view the binvox file models/binvox_files/002_master_chef_can/textured.binvox the following command should be run:

`./viewvox models/binvox_files/002_master_chef_can/textured.binvox `

[def]: https://www.patrickmin.com/binvox/
[def2]: https://www.patrickmin.com/viewvox/
