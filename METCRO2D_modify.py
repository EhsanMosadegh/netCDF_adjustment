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
input_dir = work_dir+'/inputs/METCRO2D_inputs/'
output_dir = work_dir+'/outputs/METCRO2D_output/'

########################################

favorite_value = 0.001
nc_variable = 'LAI'

input_file_name = 'METCRO2D_160711.nc'
input_file_full_path = os.path.join( input_dir , input_file_name)

# read the netcdf file
nc_file = Dataset( input_file_full_path ,'r+')

LAI_VAR = nc_file.variables[ nc_variable ]

print('-> LAI dimensions are = ' , LAI_VAR.dimensions )
print('-> size of each dim is = ' , LAI_VAR.shape )

tstep_Ubound = LAI_VAR.shape[0]
lay_Ubound = LAI_VAR.shape[1]
row_Ubound = LAI_VAR.shape[2]
col_Ubound = LAI_VAR.shape[3]


for itstep in range(0,tstep_Ubound,1):

    for ilay in range(0,lay_Ubound,1):

        for irow in range(0,row_Ubound,1):

            for icol in range(0,col_Ubound,1):

                if ( LAI_VAR[ itstep , ilay , irow , icol ] == 0 ):

                    print( '-> there are zero valus in %s' %(input_file_name) )
                    print( '-> we will replace zero values with %s' %(favorite_value) )

                    LAI_VAR[ itstep , ilay , irow , icol ] = favorite_value

                #else:

                    	#print( '-> there was not any zero inside %s' %(input_file_name) )
nc_file.close()

########################################
# QA to check if there is still zero:

# select a subset of LAY array

print('-> doing the QA to check if there is any zero left...')

nc_file = Dataset( input_file_full_path ,'r')

LAI_VAR = nc_file.variables[ nc_variable ]

LAI_array = np.array( LAI_VAR[:,:,:,:] )

if ( np.amin(LAI_array) == 0 ) :

	print( '-> ERROR: there are still zero valus in %s' %(input_file_name) )

else:

	print( '-> no zero value found inside %s' %(input_file_name) )

nc_file.close()