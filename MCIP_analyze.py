#!/usr/bin/env python3

# Created on Thu Feb  20, 2019
# @author: ehsan
##################

from netCDF4 import Dataset
import numpy as np
#import os
#from shutil import copyfile

##################

metVariable = 'LAI'  # RN
#tstep = 1
lay = 0

fileName = 'METCRO2D_160913.copied'
#filePath = '/data/gpfs/assoc/amg/MCIP_4.3/mcip_output/USFS_WRF_Tahoe_MCIPout/'
filePath = '/Users/ehsan/Documents/Python_projects/netCDF_modify/inputs/METCRO2D_inputs/'

fileNameFullPath = filePath + fileName
print('-> file name full path is: %s' %(fileNameFullPath))

inputFile = Dataset( fileNameFullPath, 'r')

ncVariable = inputFile.variables[metVariable]
print('-> looking at METCRO2D variable: %s:' %( ncVariable.long_name ))
print('-> %s = %s' %( ncVariable.long_name , ncVariable.var_desc))

numTimeSteps = ncVariable.shape[0]
rowUpperBound = ncVariable.shape[2]
colUpperBound = ncVariable.shape[3]
ncUnit = ncVariable.units

for tstep in range(0,numTimeSteps,1):

    domainCellsValueList = []

    for row in range(0,rowUpperBound,1):

        for col in range(0,colUpperBound,1):

            cellValue = ncVariable[ tstep , lay , row , col ]

            domainCellsValueList.append(cellValue)

    cellValueArray = np.array(domainCellsValueList)

    print('-> at time-step: %s' %(tstep))
    print('-> min value of var (%s) is = %s, %s'%( metVariable , cellValueArray.min(), ncUnit ) )
    print('-> max value of var (%s) is = %s, %s'%( metVariable , cellValueArray.max(), ncUnit ) )

inputFile.close()