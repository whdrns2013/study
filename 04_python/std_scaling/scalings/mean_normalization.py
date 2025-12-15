# mean normalization
data = [-100, -90, -50, -40, 25, 25]
x_mean = sum(data)/len(data)
x_max = max(data)
x_min = min(data)
scaled_data = [(x - x_mean)/(x_max - x_min) for x in data]
print(scaled_data)