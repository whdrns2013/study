# standard scaling
data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)
std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
z_score_scaled = [(x - mean) / std for x in data]
print(z_score_scaled)

# standard scaling
from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[10], [20], [30], [40], [50]])
scaler = StandardScaler()
z_score_scaled = scaler.fit_transform(data)
print(z_score_scaled.flatten())