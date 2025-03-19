
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
#matplotlib.pyplot.scatter()

mpg = data[:, 0]
hp = data[:, 3]
wt = data[:, 5]
cyl = data[:, 1]

filter_cyl_6 = cyl == 6
filtered_mpg_cyl_6 = mpg[filter_cyl_6]

print(np.min(filtered_mpg_cyl_6))
print(np.max(filtered_mpg_cyl_6))
print(np.mean(filtered_mpg_cyl_6))

print(mpg.min())
print(mpg.max())
print(np.mean(mpg))

plt.scatter(mpg, hp, s=wt*10, color='blue')

plt.xlabel('Potrosnja(mpg)')
plt.ylabel('Konjske snage(hp)')
plt.title('drugi zadatak')

plt.show()