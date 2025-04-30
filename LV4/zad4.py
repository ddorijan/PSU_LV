import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

cf=df.sort_values("selling_price")

print(cf.head(1)) 
print(cf.tail(1))

print(cf["year"].value_counts().get(2012,0))

gg=cf[["km_driven","fuel"]]
suma_diesel=0
brojac_diesel=0
suma_ben=0
brojac_ben=0
brojac=0

for brojac in range (0,len(gg)):

    if(gg["fuel"].get(brojac)=="Diesel"):
        suma_diesel+=gg["km_driven"].get(brojac)
        brojac_diesel+=1

    elif(gg["fuel"].get(brojac)=="Petrol"):
        suma_ben+=gg["km_driven"].get(brojac)
        brojac_ben+=1


    

print(suma_ben/brojac_ben)
print(suma_diesel/brojac_diesel)

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)





#tabcorr = df.corr()
#sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

plt.show()