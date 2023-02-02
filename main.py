import binvox_rw
import os

root_directory = os.path.join("models","binvox_files")
file_directory = os.path.join(root_directory,"002_master_chef_can","textured.binvox")
# file_directory = os.path.join(file_directory,"textured.binvox")
with open(file_directory, 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

print(model.dims)
print(model.scale)
print(model.translate)
print(model.data)
