# MaxAbs scaling
data = [-100, 50, 90, 80, -40]
abs_max = max([abs(x) for x in data])
scaled_data = [x/abs_max for x in data]
print(scaled_data)

# MaxAbs scaling
from sklearn.preprocessing import MaxAbsScaler

data = [[-100], [50], [90], [80], [-40]]
scaler = MaxAbsScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data.flatten())