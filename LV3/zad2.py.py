import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')


sorted = mtcars.sort_values(by='cyl')
cyl = sorted.iloc[:,2:3]
mpg = sorted.iloc[:,1:2]
vector = np.vectorize(np.int_)
cyl = np.array([cyl])
x = vector(cyl)

vector = np.vectorize(np.int_)
mpg = np.array([mpg])
y = vector(mpg)
#cyl = [sorted.cyl.to_numpy()]
mpg = [sorted.mpg.to_numpy()]


plt.bar(x, y)
plt.title('Fruit Sales')
plt.xlabel('Cylinders')
plt.ylabel('mpg')
plt.show()