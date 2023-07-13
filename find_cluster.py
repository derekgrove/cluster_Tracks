#should sort through an array (256x256, size of pixel) and locate two things: skirt, core
#once those are found, should determine the major length and minor length
#maybe we remove the delta rays here as well, do this with with a morphology operator
import matplotlib.pyplot as plt
import numpy as np
 
filename = 'cluster_data.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)
print(data)
