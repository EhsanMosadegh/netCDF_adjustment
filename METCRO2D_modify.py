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
# function

def metcro2d_modify ( met_file_full_path ):

        print('-> copy the netcdf file')

        # read the copied netcdf file
        nc_file = Dataset( met_file_full_path ,'r+')

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

                            print( '-> there are zero valus at TSTEP=%s, LAY=%s, ROW=%s, COL=%s, and we will replace zero values with %s' %(itstep,ilay,irow,icol,favorite_value) )

                            LAI_VAR[ itstep , ilay , irow , icol ] = favorite_value

                        #else:

                            	#print( '-> there was not any zero inside %s' %(input_file_name) )
        nc_file.close()

########################################
# function
# QA to check if there is still zero:
# select a subset of LAY array

def metcro2d_QA (met_file_full_path):

        print('-> doing the QA to check if there is any zero left...')

        nc_file = Dataset( met_file_full_path ,'r')

        LAI_VAR = nc_file.variables[ nc_variable ]

        LAI_array = np.array( LAI_VAR[:,:,:,:] )

        if ( np.amin(LAI_array) == 0 ) :

        	print( '-> ERROR: there are still zero valus in %s' %(input_file_name) )

        else:

        	print( '-> no zero value found inside %s' %(input_file_name) )

        nc_file.close()

########################################
# set paths

work_dir = '/Users/ehsan/Documents/Python_projects/netCDF_modify'
repository_name = 'netCDF_adjustment'

script_dir = work_dir+'github/'+repository_name
input_dir = work_dir+'/inputs/METCRO2D_inputs/'
output_dir = work_dir+'/outputs/METCRO2D_output/'

########################################

favorite_value = 1e-30
nc_variable = 'LAI'
yr = '16'

########################################

month_list = [ '07' , '08' , '09' , '10' , '11' ]

for imonth in month_list :

    if ( imonth == '07' or imonth == '08' or imonth == '10' ) :

        for iday in range(1,32) :

            if ( iday <= 9 ) :

                iday = '0'+str(iday)

                #print('iday is %s' %iday)

            else:

                iday = str(iday)

            date_tag = yr+imonth+iday

            input_file_name = 'METCRO2D_'+date_tag+'.nc'

            print('-> input file is %s' %input_file_name)

            input_file_full_path = os.path.join( input_dir , input_file_name)

            if ( os.path.isfile(input_file_full_path) == False ):

                print('-> %s not available, go to the next file' %(input_file_name) )
                continue

            else:
                print('-> %s exists, and will be modified' %( input_file_name) )
                #metcro2d_modify( input_file_full_path)
                #metcro2d_QA ( input_file_full_path)



    elif ( imonth == '09' or imonth == '11') :

        for iday in range(1,31) :

            if ( iday <= 9 ) :

                iday = '0'+str(iday)

            else:

                iday = str(iday)

            date_tag = yr+imonth+iday

            input_file_name = 'METCRO2D_'+date_tag+'.nc'

            print('-> input file is %s' %input_file_name)

            input_file_full_path = os.path.join( input_dir , input_file_name)

            if ( os.path.isfile(input_file_full_path) == False ):

                print('-> %s not available, go to the next file' %(input_file_name) )
                continue

            else:
                print('-> %s exists, and will be modified' %( input_file_name) )
                #metcro2d_modify( input_file_full_path)
                #metcro2d_QA ( input_file_full_path)

    else:

        print('-> month not used, check month number')

print('***** SUCCESSFULL FINISH *****')


