#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################
# Created on Sat Dec  8 20:17:37 2018
#
# author: ehsan (ehsanm@dri.edu)
########################################

from netCDF4 import Dataset
import numpy as np

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

nc_file = Dataset(file_name_path , 'r')

var_keys = np.array([])

var_keys = nc_file.variables.keys()

print('-> size of var_keys list is %s' %var_keys.size)

for ivar in nc_file.variables.keys():

    print(ivar)
