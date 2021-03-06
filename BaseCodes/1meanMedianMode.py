# -*- coding: utf-8 -*-
"""
@author: PROTIK
"""

import numpy as np
from scipy import stats as st

data = np.array([4, 5, 1, 2, 7, 2, 6, 9, 3])

dt_mean = np.mean(data)
print(f'Mean of Data: {dt_mean}')

dt_median = np.median(data)
print(f'Median of the data: {dt_median}')

dt_mode = st.mode(data, axis=None)
print(f'Mode of the Data: {dt_mode}')