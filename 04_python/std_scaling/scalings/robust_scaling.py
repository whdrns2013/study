# Robust Scaling
import numpy as np

data = [10, 20, 30, 40, 100]  # 이상치 포함

# 중앙값과 IQR 계산
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
median = np.median(data)
iqr = q3 - q1

# Robust 표준화
robust_scaled = [float((x - median) / iqr) for x in data]
print(robust_scaled)


# Robust Scaling
from sklearn.preprocessing import RobustScaler

data = np.array([[10], [20], [30], [40], [100]])

scaler = RobustScaler()
robust_scaled = scaler.fit_transform(data)

print(robust_scaled.flatten())
