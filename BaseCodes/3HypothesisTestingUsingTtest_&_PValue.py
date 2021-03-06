# -*- coding: utf-8 -*-
"""
@author: PROTIK
"""

from scipy import stats
import numpy as np

xbar = 990
miu = 1000
s = 12.5
n = 30
alpha = 0.05

#Test Statistics
z_calculate = (xbar - miu) / (s / np.sqrt(float(n)))
print("Test statistics Value: ", round(z_calculate, 2))

#critical Z value from table
z_critical = stats.t.ppf(alpha, n - 1)
print("Critical Z value from Table: ", round(z_critical, 2))

#p-value calculation
p_val = stats.t.sf(np.abs(z_calculate), n - 1)
print("P-value of the example: ", p_val)

#validation using z value
print("Using the Z value")
if (z_critical > z_calculate):
    print(
        "Based on the existed evidance in hand, we can reject the null hypothesis"
    )
else:
    print("Accept the hypothesis")

#validation using P-Value
print("Using the P value")
if (alpha > p_val):
    print(
        "Based on the existed evidance in hand, we can reject the null hypothesis"
    )
else:
    print("Accept the hypothesis")