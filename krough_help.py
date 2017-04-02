from scipy.interpolate import KroghInterpolator
#from format_data import Formatter
import matplotlib.pyplot as plt
import time
import numpy as np

x_values = [1,2,3,4,5]
y_values = [6,7,8,9,10]
intra_x_values = [6,7,8]

poly_func = KroghInterpolator(x_values,y_values)
intra_x_values = np.asarray(intra_x_values)
intra_y_values = poly_func.__call__(intra_x_values)
print(intra_y_values)
