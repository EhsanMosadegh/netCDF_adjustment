#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:18:28 2019

@author: ehsan (ehsanm@dri.edu)
"""

##########

from netCDF4 import Dataset
from shutil import copyfile
import os

##########
# set favorite parameters
tstep = 0
lay = 0
favoriteValue = 0.0

# read the file
inputFileDirectory = '/Users/ehsan/Documents/Python_projects/netCDF_modify/inputs/'
fileBaseName = 'ocean_file_CA_WRF_1km_original'
fileFullName = fileBaseName+'.ncf'

fileNameFullPath = inputFileDirectory + fileFullName
print('-> file name full path is: %s' %(fileNameFullPath) )

if ( os.path.isfile(fileNameFullPath) == False):
    print('-> input file not available, or path is incorrect!')
    raise SystemExit()

# copy the file
oceanFileCopiedName = fileBaseName + '.zero' + '.ncf'
oceanFileCopiedPath = inputFileDirectory
oceanFileCopied = oceanFileCopiedPath + oceanFileCopiedName

copyfile( fileNameFullPath , oceanFileCopied )

# read copied netCDF file
oceanFile = Dataset( oceanFileCopied , 'r+')  # r+ enables inplace modification

# define variables
oceanVarList = ['SURF' , 'OPEN']

# loop through row and columns
for listVar in oceanVarList:
    oceanVar = oceanFile.variables[listVar]
    print('-> modifying values to zero for: %s' %(listVar))

    rowUpBound = oceanVar.shape[2]
    colUpBound = oceanVar.shape[3]

    for row in range(0,rowUpBound,1):
        for col in range(0,colUpBound,1):

            oceanCellValue = oceanVar[ tstep, lay, row, col ]

            if ( oceanCellValue == favoriteValue ):
                continue

            else:
                print('-> for row:%s, col:%s, zero replaced %s' %( row, col, oceanCellValue) )
                oceanVar[ tstep, lay, row, col ] = 0.0
                
print('-> end of program!')
oceanFile.close()
