## Author: Wiebe van Breukelen

import numpy as np
import numpy.random
import matplotlib.pyplot as plt
 
# Graph size
extent = [0, 2, 0, 3]

# Initialize empty array
data = numpy.zeros((3, 2))


## Wi-Fi Results
#data[0][0] = 2.63 # Top-left
data[0][0] = 1.31
#data[0][1] = 1.05 # Top-right
data[0][1] = 1.90
#data[1][0] = 0.60 # Middle-left
data[1][0] = 1.27
#data[1][1] = 2.46 # Middle-right
data[1][1] = 1.85
#data[2][0] = 1.03 # Bottom-left
data[2][0] = 1.50
#data[2][1] = 0.52 # Bottom-right
data[2][1] = 1.25
#data[1][1] = 2.72 # Center (5 cm)
data[1][1] = 2.72


## Bluetooth Results
#data[0][0] = 27.95 # Top-left
#data[0][0] = 21.73
#data[0][1] = 32.19 # Top-right
#data[0][1] = 32.05
#data[1][0] = 30.59 # Middle-left
#data[1][0] = 32.20
#data[1][1] = 32.44 # Middle-right
#data[1][1] = 32.33
#data[2][0] = 32.47 # Bottom-left
#data[2][0] = 32.57
#data[2][1] = 29.82 # Bottom-right
#data[2][1] = 29.73
#data[1][1] = 32.20 # Center (5 cm)
#data[1][1] = 32.20

plt.clf()
#plt.title('Bluetooth transfer rate in environment')
plt.ylabel('y')
plt.xlabel('x')
plt.axis('off')
# Using interpolation, fill in gaps between our set points
plt.imshow(data, vmin=0, vmax=3, interpolation='bicubic', cmap='RdYlBu_r', extent=extent, alpha=1) # vmin=0, vmax=3 for wifi, vmin=20, vmax=30 for bluetooth
plt.colorbar().ax.set_ylabel("MB/s")
plt.savefig("test.png", bbox_inches='tight')
plt.show()
