# -*- coding: utf-8 -*-
"""
@author: PROTIK
"""

from statistics import variance, stdev
import numpy as np

game_points = np.array(
    [35, 56, 43, 59, 63, 79, 35, 41, 64, 43, 93, 60, 77, 24, 82])

#variance
data_variance = variance(game_points)
print("Sample variance:", round(data_variance, 2))

#standard deviation
data_stdev = stdev(game_points)
print("Sample std.dev:", round(data_stdev, 2))

#calculate range
data_range = np.max(game_points) - np.min(game_points)
print("Data Range: ", data_range)

#calculate percentile
print("Quartiles:")
for val in [25, 50, 75, 100]:
    data_quartile = np.percentile(game_points, val)
    print(str(val) + "%", data_quartile)

#calculate IQR
q75, q25 = np.percentile(game_points, [75, 25])
print("Inter Quartile Range: ", q75 - q25)