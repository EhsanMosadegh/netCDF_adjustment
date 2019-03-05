#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:15:23 2019

@author: ehsan
"""
##################

from netCDF4 import Dataset
import numpy as np
import os
from shutil import copyfile

##################
nc_variable_list = ['SURF' , 'OPEN']


nc_file_name = 'ocean_file_CA_WRF_1km.ncf'
nc_file_path = '/Users/ehsan/Documents/Python_projects/netCDF_modify/inputs/'
nc_file_full_path = nc_file_path + nc_file_name

ocean_file_copied = nc_file_full_path + '.copied'

copyfile( nc_file_full_path , ocean_file_copied )

input_file = Dataset( ocean_file_copied, 'r+')

