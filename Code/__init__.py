#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2022/05/16
@Author  :   Jeff H
@Contact :   windminim@outlook.com
@Department   :  Windminim Studio
@Desc    :   Initialization of all the required libraries and basic configurations.
'''

# here put the import lib

import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import geatpy
import sklearn as skl
import yaml
import json


# basic paths and variables

about_author = "Jeff H @ Windminim Studio"
about_email = "windminim@outlook.com"
about_page = "https://da2la.github.io/"
about_version = "0.1"

dir_conf = "../Config/"             # Configurations
dir_code = "../Code/"               # All the codes
dir_resource = "../Resource/"       # Resources (Images, plugins, etc.)
dir_sheet = "../Sheet/"             # Table sheets


# global prefix 
pEG = "eg_"                         # Example

