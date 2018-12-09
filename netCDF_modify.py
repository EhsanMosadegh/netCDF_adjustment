#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################
# Created on Sat Dec  8 20:17:37 2018
#
#@author: ehsan
########################################

from netCDF4 import Dataset

########################################

work_dir = '/Users/ehsan/Documents/PYTHON_CODES/netCDF_modify'
repository_name = 'netCDF_adjustment'
script_dir = work_dir+'/github/'+repository_name
input_dir = work_dir+'/inputs'
output_dir = work_dir+'/outputs'

########################################

file_name = 'filename'

file_path = 'filepath'

file_name_path = file_name+file_path

nc_input_file = Datasetset(file_name_path , 'r')