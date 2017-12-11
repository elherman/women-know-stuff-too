
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import mpld3

with open('file_name') as f:
	content = [x.strip('\n') for x in f.readlines()]
	print(content)
str(content)
my_dict = {}
my_dict = dict(s.split(' - ') for s in content)
print(my_dict)

for k, v in my_dict.items():
    print(k,v)

for k, v in my_dict.items():
    k = x_values
    v = y_values

print(x_values)

#plt.plot(x, y)
#plt.show()

#coordinates = my_dict.items()
#y, x = zip(*coordinates)
x_coordinates = []
for x in my_dict:
	x_coordinates.append(x)

	
print(x_coordinates)

#same thing doesn't work to produce y-coordinates (number values)
