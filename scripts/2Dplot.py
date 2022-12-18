import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv(r'C:\Users\tagir\Documents\![Crazyflie Flight Tests]\![From Github]\APFforCircularMotion\data\most valuable\20221217-161835_apf3.csv', header=0, delimiter=';')

cols = df.columns
for col in cols:
    df[col] = df[col].astype(float)

print(df.columns)



# df.plot(x='i', y=['setPx1','setPx2','setPx3'])
# df.plot(x='i', y=['setPy1','setPy2','setPy3'])
# df.plot(x='i', y=['p_12', 'p_23'])
ax = df.plot(x='i', y=['p12_APF', 'p23'])
ax.set(xlabel='Time, [ds]', ylabel='Phase shifts, [rad]')

ax = df.plot(x='i', y=['distance_12'])
ax.set(xlabel='Time, [ds]', ylabel='Distance between UAVs, [rad]')

# df.plot(x='i', y=['d_1','d_2', 'd_3'])
ax = df.plot(x='i', y=['d_1','d_2', 'd_3'])
ax.set(xlabel='Time, [ds]', ylabel='Distances to the center, [m]')
# df.plot(x='px_1', y=['py_1'])
# df.plot(x='px_2', y=['py_2'])
# ax = df.plot(x='px_1', y=['py_1'])
# df.plot(x='px_2', y=['py_2'], ax=ax)

fig, axes = plt.subplots(nrows=3, ncols=1)
ax=df.plot(x='px_1', y=['py_1'], ax=axes[0])
ax.set(xlabel='px_1, [m]', ylabel='py_1, [m]')

ax=df.plot(x='px_2', y=['py_2'], ax=axes[1])
ax.set(xlabel='px_2, [m]', ylabel='py_2, [m]')

ax=df.plot(x='px_3', y=['py_3'], ax=axes[2])
ax.set(xlabel='px_3, [m]', ylabel='py_3, [m]')
# df.plot(x='setPx3', y=['setPy3'])
plt.show()
