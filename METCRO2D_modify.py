#!/usr/bin/env python3

########################################
# created on: Jan 14, 2019
#
# author: ehsanm (ehsanm@dri.edu)
# Purpose: to manipulate METCDRO2D values
########################################

from netCDF4 import Dataset
import numpy as np
import os

########################################

work_dir = '/Users/ehsan/Documents/Python_projects/netCDF_modify'
repository_name = 'netCDF_adjustment'
script_dir = work_dir+'github/'+repository_name
input_dir = work_dir+'inputs/METCRO2D_inputs/'
output_dir = work_dir+'outputs/METCRO2D_output'

########################################

favorite_value = 0.001
nc_variable = 'LAI'

input_file_name = 'METCRO2D_160711.nc'
input_file_full_path = os.path.join( input_dir , input_file_name)

# read the netcdf file
nc_file = Dataset( input_file_full_path ,'r+')

if ( nc_file.nc_variables[ nc_variable ] == 0 ) :

	print( '-> there are zeros in %s' %(input_file_name) )
	print( '-> we will replace zero values with %s' %(favorite_value) )

	nc_file.nc_variables[ nc_variable ][:] = favorite_value

else:

	print( '-> there was not any zero inside %s' %(input_file_name) )

nc_file.close()