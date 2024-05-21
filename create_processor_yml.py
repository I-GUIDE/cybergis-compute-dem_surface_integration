#!/bin/env python3

import yaml
import os

#input_dir = '/compute_scratch/%s' % os.environ['param_input_dir']
#processor_dict ={'$1': {'SimpleDataProc':{'input_dir':input_dir, 'start_year': os.environ['param_start_year'],'end_year': os.environ['param_end_year']}}}
processor_dict ={'$1': {'DEM_surface_integration':{'mesh_file': os.environ['param_mesh_file'],'boundary_file': os.environ['param_boundary_file'], 'dem_file':os.environ['param_dem_file']}}}



with open('/job/executable/rastertools.yml','w') as dem_surface_integration_file:
    yaml.dump(processor_dict,dem_surface_integration_file)
