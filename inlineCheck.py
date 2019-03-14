#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:03:12 2019

@author: ehsan
"""
from netCDF4 import Dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# set pathes to files
ncFilePath = '/Users/ehsan/Documents/Python_projects/USFS_fire/outputs/'
ncFileName = 'inln_mole_ptfire_20160901_Landis_yr30_scen1_cmaq_cb6_2011ek_cb6v2_v6_11g.ncf'
ncFile = ncFilePath + ncFileName

# read in nc file
inputFile = Dataset( ncFile , 'r')

# select a variable to check
inlnVar = 'NO'
ncVar = inputFile.variables[ inlnVar ]

# print no. of sources = ROW variable in netCDF file
print('-> no. of sources: %s' %( ncVar.shape[2]) )

# setting for hand picked samples
tstep = 1
lay = 0
row = 1  # no. of sources/ meaning no. of fires in a file?
col = 0  # always 1, constant

#ncVarExtract = ncVar[tstep , lay , row , col]

#noOfSource = 1  # row
tstepList = range(0,25,1)

# 4D variables: float32 CO(TSTEP, LAY, ROW, COL)
srcSeries1 = ncVar[:,0,0,0]
srcSeries2 = ncVar[:,0,1,0]
#srcSeries3 = ncVar[:,0,2,0]

# plot 2 time series
plt.plot(tstepList , srcSeries1 , lw=2 , label = 'src1' )
plt.plot(tstepList , srcSeries2 , lw=2 , label = 'src2' )
#plt.plot(tstepList , srcSeries3 , lw=2 , label = 'src3' )

# set range of x ticks range
plt.xticks(np.arange(0,25,1))

plt.xlabel('timeStep (hr)')
plt.ylabel(inlnVar)
plt.title(ncFileName)
plt.legend()
plt.show()

#pathToSave = '/Users/ehsan/Documents/Python_projects/USFS_fire/outputs'
#plt.save(pathToSave)