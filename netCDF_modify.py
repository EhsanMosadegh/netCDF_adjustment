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

file_name = 'BCON_v521_test_for_v53_profile'

file_path = '/Users/ehsan/Documents/PYTHON_CODES/netCDF_modify/inputs/'

file_name_path = file_path+file_name

print( '-> file name is "%s" ' %file_name )
print( '-> file path is "%s"' %file_path )
print( '-> file name and path is "%s"' %file_name_path )

nc_input_file = Dataset(file_name_path , 'r')