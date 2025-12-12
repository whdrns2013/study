# decimal scaling
from math import pow

data = [-10230, 48273, 1836, 28462, -100000]
d = len(str(max([abs(x) for x in data]))) - 1
scaled_data = [x/pow(10, d) for x in data]
print(scaled_data)