import numpy as np
height=([1.73,1.68,1.71,1.89,1.79])
np_height=np.array(height)
print(np_height)
weight=([65.4,59.2,63.6,88.4,68.7])
np_weight=np.array(weight)
print(np_weight)

bmi=np_weight/np_height**2
print(bmi)
print(type(np_weight))
print(type(np_height))
