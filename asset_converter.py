# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import argparse
import asyncio
import omni
import os
from omni.isaac.kit import SimulationApp


# specify the repository folder where object_shape_completion is located
root_dir = "/home/elyar/thesis/object_shape_completion/"

async def convert(in_file, out_file, load_materials=False):
    # This import causes conflicts when global
    import omni.kit.asset_converter

    def progress_callback(progress, total_steps):
        pass

    converter_context = omni.kit.asset_converter.AssetConverterContext()
    # setup converter and flags
    converter_context.ignore_materials = not load_materials
    # converter_context.ignore_animation = False
    # converter_context.ignore_cameras = True
    # converter_context.single_mesh = True
    # converter_context.smooth_normals = True
    # converter_context.preview_surface = False
    # converter_context.support_point_instancer = False
    # converter_context.embed_mdl_in_usd = False
    # converter_context.use_meter_as_world_unit = True
    # converter_context.create_world_as_default_root_prim = False
    instance = omni.kit.asset_converter.get_instance()
    task = instance.create_converter_task(in_file, out_file, progress_callback, converter_context)
    success = True
    while True:
        success = await task.wait_until_finished()
        if not success:
            await asyncio.sleep(0.1)
        else:
            break
    return success


def asset_convert(input_dir):
    supported_file_formats = ["obj"]
    local_asset_output = input_dir + "/usd_file/"
    result = omni.client.create_folder(f"{local_asset_output}")

    print(f"\nConverting folder {input_dir}...")

    (result, models) = omni.client.list(input_dir)

    for i, entry in enumerate(models):
        model = str(entry.relative_path)
        model_name = os.path.splitext(model)[0]
        model_format = (os.path.splitext(model)[1])[1:]
        # Supported input file formats
        if model_format in supported_file_formats:
            input_model_path = input_dir + "/" + model
            converted_model_path = input_dir + "/usd_file/" + model_name + "_" + model_format + ".usd"
            if not os.path.exists(converted_model_path):
                status = asyncio.get_event_loop().run_until_complete(
                    convert(input_model_path, converted_model_path, True)
                )
                if not status:
                    print(f"ERROR Status is {status}")
                print(f"---Added {converted_model_path}")


if __name__ == "__main__":
    kit = SimulationApp()

    # specify the directory containing the folders
    models_dir = root_dir + "models/ycb_copy/"

    # loop through each folder in the directory
    # and call converter function to convert obj file to usd one
    for folder_name in os.listdir(models_dir):
        model_path = os.path.join(models_dir, folder_name)

        # Ensure Omniverse Kit is launched via SimulationApp before asset_convert() is called
        asset_convert(model_path+"/google_64k")

    # cleanup
    kit.close()