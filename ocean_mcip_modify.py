#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:18:28 2019
@author: ehsan (ehsanm@dri.edu)
purpose: to modify GRID-CRO-2D and Ocean files
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

# define variables
ncVarList = ['PURB'] #['SURF' , 'OPEN']

# read the file
inputFileDirectory = '/Users/ehsan/Documents/Python_projects/netCDF_modify/inputs/'
fileBaseName = 'GRIDCRO2D_160901'
baseFileExtenstion = '.nc'
copyFileLabel = '.PURBzero'
fileFullName = fileBaseName + baseFileExtenstion


fileNameFullPath = inputFileDirectory + fileFullName
print('-> file name full path is: %s' %(fileNameFullPath) )

if ( os.path.isfile(fileNameFullPath) == False):
    print('-> input file not available, or path is incorrect!')
    raise SystemExit()

# copy the file
ncFileCopiedName = fileBaseName + copyFileLabel + baseFileExtenstion
ncFileCopiedPath = inputFileDirectory
ncFileCopied = ncFileCopiedPath + ncFileCopiedName

copyfile( fileNameFullPath , ncFileCopied )

# read copied netCDF file
ncFile = Dataset( ncFileCopied , 'r+')  # r+ enables inplace modification

# loop through row and columns
for listVar in ncVarList:
    ncVar = ncFile.variables[listVar]
    print('-> modifying values to zero for: %s' %(listVar))

    rowUpBound = ncVar.shape[2]
    colUpBound = ncVar.shape[3]

    for row in range(0,rowUpBound,1):
        for col in range(0,colUpBound,1):

            ncFileCellValue = ncVar[ tstep, lay, row, col ]

            if ( ncFileCellValue == favoriteValue ):
                continue

            elif ( ncFileCellValue < favoriteValue ):

                print('-> for row:%s, col:%s, %s replaced %s' %( row, col, favoriteValue, ncFileCellValue) )
                ncVar[ tstep, lay, row, col ] = favoriteValue

            else:
                print('-> value for row:%s and col:%s is= %s' %( row, col, ncFileCellValue) )

print('-> end of program!')
ncFile.close()
