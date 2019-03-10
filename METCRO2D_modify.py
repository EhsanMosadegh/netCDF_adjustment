#!/usr/bin/env python3

#########################################################################################################
# created on: Jan 14, 2019
#
# author: ehsanm (ehsanm@dri.edu)
# Purpose: to manipulate METCDRO2D values
#########################################################################################################

from netCDF4 import Dataset
import numpy as np
import os
from shutil import copyfile

#########################################################################################################

yr = '16'
favoriteValue = 0.1

platformList =      [ 'MAC'         , 'HPC'         ]
platform            = platformList[0]

varFavoriteList =   [ 'LAI'         , 'PURB'        ]
mcipFileList =      [ 'METCRO2D'    , 'GRIDCRO2D'   ]
copyNameTagList =   [ '_LAIpoint1'  , '.PURBzero'   ]

varFavorite         = varFavoriteList[1]
mcipFileToAnalyze   = mcipFileList[1]
copyNameTag         = copyNameTagList[1]

#########################################################################################################
# set paths

if ( platform == 'MAC') :

    work_dir = '/Users/ehsan/Documents/Python_projects/netCDF_modify/'
    repository_name = 'netCDF_adjustment'
    script_dir = work_dir+'github/'+repository_name
    input_dir = work_dir+'inputs/'
    output_dir = work_dir+'outputs/mcipFileToAnalyzeoutput/'

elif ( platform == 'HPC') :

    work_dir = '/data/gpfs/assoc/amg/MCIP_4.3/mcip_output/USFS_WRF_Tahoe_MCIPout'
    repository_name = '/netCDF_adjustment'
    script_dir = work_dir+repository_name
    input_dir = work_dir  # point to where METCRO2D files are
    #output_dir = work_dir

else:

    print('-> ERROR: platform is not set, exiting...')
    raise SystemExit()

print('-> current directory is: "%s"' %(os.getcwd()) )
#print('-> changing directory to where METCRO2D files are...')
#os.chdir( work_dir )
#print('-> now we are at:')
#print('-> %s' %( os.getcwd() ))

#########################################################################################################
# function

def modifyMcipFile ( copiedMcipFile ):

        print('-> start modify MCIP file...')

        # read the copied netcdf file
        mcipFile = Dataset( copiedMcipFile ,'r+')

        varToModify = mcipFile.variables[ varFavorite ]

        print('-> LAI dimensions are = ' , varToModify.dimensions )
        print('-> size of each dim is = ' , varToModify.shape )

        tstep_Ubound = varToModify.shape[0]
        lay_Ubound = varToModify.shape[1]
        row_Ubound = varToModify.shape[2]
        col_Ubound = varToModify.shape[3]


        for timeStep in range(0,tstep_Ubound,1):

            for layerStep in range(0,lay_Ubound,1):

                for rowStep in range(0,row_Ubound,1):

                    for colStep in range(0,col_Ubound,1):

                        if ( varToModify[ timeStep , layerStep , rowStep , colStep ] == 0 ): # replace happens

                            #print( '-> there are zero valus at TSTEP=%s, LAY=%s, ROW=%s, COL=%s, and we will replace zero values with %s' %(timeStep,layerStep,rowStep,colStep,favoriteValue) )

                            varToModify[ timeStep , layerStep , rowStep , colStep ] = favoriteValue

                        else:

                            	#print( '-> there was not any zero inside %s' %(inputFileName) )
                             continue
        mcipFile.close()

#########################################################################################################
# function
# QA to check if there is still zero:
# select a subset of LAY array

def qualityCheckMcipFileModified ( copiedMcipFile ):

        print('-> now perform QA to check if any zero is left...')

        mcipFile = Dataset( copiedMcipFile ,'r')

        varToModify = mcipFile.variables[ varFavorite ]

        LAI_array = np.array( varToModify[:,:,:,:] )

        if ( np.amin(LAI_array) == 0 ) :

            print( '-> ERROR: there are still zero valus in %s' %(inputFileName) )

        else:

            print( '-> no zero value found inside %s' %(inputFileName) )

        mcipFile.close()

#########################################################################################################

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

            inputFileName = mcipFileToAnalyze+'_'+date_tag

            print('===> processing file: %s' %inputFileName)

            InputFileFullPath = os.path.join( input_dir , inputFileName )

            if ( os.path.isfile(InputFileFullPath) == False ):

                print('-> %s NOT in input directory, go to the next file' %(inputFileName) )
                continue

            else:

                print('-> %s exists, and will be modified' %( inputFileName) )

                print('-> copy the met file...')

                copiedMcipFile = InputFileFullPath + copyNameTag

                copyfile( InputFileFullPath , copiedMcipFile )

                modifyMcipFile( copiedMcipFile)

                qualityCheckMcipFileModified ( copiedMcipFile)



    elif ( imonth == '09' or imonth == '11') :

        for iday in range(1,31) :

            if ( iday <= 9 ) :

                iday = '0'+str(iday)

            else:

                iday = str(iday)

            date_tag = yr+imonth+iday

            inputFileName = mcipFileToAnalyze+'_'+date_tag

            print('===> processing file: %s' %inputFileName)

            InputFileFullPath = os.path.join( input_dir , inputFileName )

            if ( os.path.isfile(InputFileFullPath) == False ):

                print('-> %s NOT available, go to the next file' %(inputFileName) )
                continue

            else:

                print('-> %s exists, and will be modified' %( inputFileName) )

                print('-> copy the met file...')

                copiedMcipFile = InputFileFullPath + copyNameTag

                copyfile( InputFileFullPath , copiedMcipFile )

                modifyMcipFile( copiedMcipFile)

                qualityCheckMcipFileModified ( copiedMcipFile)

    else:

        print('-> month not used, check month number')

print('***** SUCCESSFULL FINISH *****')


