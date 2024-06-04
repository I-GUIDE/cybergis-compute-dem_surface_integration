from rastertools import *
import os
from glob import glob
import warnings
import sys
warnings.filterwarnings("ignore")


mesh_file = sys.argv[1]
boundary_file=sys.argv[2]
dem_file=sys.argv[3]

folder = os.path.dirname(os.path.dirname(mesh_file))
output_folder = folder + "/output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
surface_file = output_folder + "/surface.tif"
merged_file = output_folder + "/merged.tif"

value_type = 'depth-' if ('brazos' in folder) else 'depth+'

interpolate_points_to_raster(mesh_file=mesh_file,
                                 surface_file=surface_file,
                                 boundary_file=boundary_file,
                                 resolution=5)

integrate_surface_with_dem(surface_file=surface_file,
                               dem_file=dem_file,
                               merged_file=merged_file,
                               value_type=value_type,
                               resolution=5)


