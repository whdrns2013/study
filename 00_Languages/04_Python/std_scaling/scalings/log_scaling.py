from math import log

data = [81, 243, 729, 2187]
scaled_data = [log(x) for x in data]
print(scaled_data)