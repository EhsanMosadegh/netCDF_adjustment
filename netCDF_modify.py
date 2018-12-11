#!/usr/bin/env python3

########################################
# Created on Sat Dec  8 20:17:37 2018
#
# author: ehsan (ehsanm@dri.edu)
# purpose:
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
print( '-> file path is "%s" ' %file_path )
print( '-> file name and path is "%s" ' %file_name_path )

nc_file = Dataset(file_name_path , 'r+')

#nc_file_modified = nc_file.copy()

var_keys = []

for ivar in nc_file.variables.keys():

	var_keys.append(ivar)

var_keys_array = np.array(var_keys)

print('-> size of var_keys list is : %s ' %var_keys_array.size)

#nc_var_array = np.array([])

for var_key in var_keys_array :

	print('-> doing for %s ...'  %var_key)

	nc_var = nc_file.variables[var_key]

	if nc_var.name == 'TFLAG' :

		print('-> VAR is TFLAG, we do not need it, so we pass!')

		continue

		#print('-> for %s variable, shape is %s and dtype is %s'  %( nc_var.name , nc_var.shape , nc_var.dtype))

	datatype = nc_var.dtype

	if datatype == 'float32' :

		nc_var[:] = 0.000

	else:

		print('-> dtype is NOT "float32", check the dtype for %s '  %nc_var.name  )

print('--------------------------------------------------------------')
print('-> doing QA check on arrays ...')

for var_key in var_keys_array :

	var_max = np.amax( nc_file.variables[ var_key ] ) 

	if var_max == 0 :

		print( '-> QA checked, all elements inside (%s) array are now zero! ' %var_key)

	else:

		print( '-> NOTE: there are still non-zero elements for (%s), go back and check!' %var_key)

nc_file.close()
