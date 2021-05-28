import numpy as np

# ローターの大きさを半径で指定
R=50.0
# ステーショナリギアとインナーギアの中心差分を指定
e=10.0
# 分割数
s=120.0

t=2.0*np.pi/s
for q in np.arange(0.0, 2.0*np.pi*3.0, t):
    q3 = q / 3.0
    px = e * np.cos(q) + R * np.cos(q3)
    py = e * np.sin(q) + R * np.sin(q3)
    print(str(px)+','+str(py))
