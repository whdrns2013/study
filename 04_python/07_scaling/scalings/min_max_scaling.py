# Min Max Scaling
from typing import List

class CustomMinMaxScaler:
    def __init__(self, data:List[int]):
        self.data = data
        self.min = min(data)
        self.max = max(data)
    
    def scaling(self):
        return [(x - self.min)/(self.max - self.min) for x in self.data]

data = [50, 90, 69, 80, 100]
scaler = CustomMinMaxScaler(data)
scaled_data = scaler.scaling()
print(scaled_data)

# Min Max Scaling
def custom_minmax_scaling(data:List[int]):
    max_val = max(data)
    min_val = min(data)
    result = [(x - min_val)/(max_val - min_val) for x in data]
    return result

data = [50, 90, 69, 80, 100]
scaled_data = custom_minmax_scaling(data)
print(scaled_data)

# Min Max Scaling
from sklearn.preprocessing import MinMaxScaler

data = [[50], [90], [69], [80], [100]]
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data.flatten())