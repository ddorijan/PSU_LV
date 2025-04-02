import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Učitavanje podataka
df = pd.read_csv('occupancy_processed.csv')

# Definicija značajki i ciljne varijable
feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

# Podjela podataka na trening i testni skup (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Skaliranje podataka (KNN je osjetljiv na razmjere značajki)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Testiranje različitih vrijednosti K
k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))

plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='dashed')
plt.xlabel('Broj susjeda (K)')
plt.ylabel('Točnost')
plt.title('Utjecaj broja susjeda na točnost KNN modela')
plt.show()

# Treniranje KNN modela s optimalnim K (npr. 5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predikcija na testnom skupu
y_pred = knn.predict(X_test)

# Evaluacija modela
accuracy = accuracy_score(y_test, y_pred)
print(f'Točnost modela: {accuracy:.2f}')

# Prikaz matrice zabune
conf_matrix = confusion_matrix(y_test, y_pred)
print('Matrica zabune:')
print(conf_matrix)

plt.figure(figsize=(5, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predviđene vrijednosti')
plt.ylabel('Stvarne vrijednosti')
plt.title('Matrica zabune')
plt.show()

# Izvještaj klasifikacije
print('Izvještaj klasifikacije:')
print(classification_report(y_test, y_pred, target_names=class_names))

# Vizualizacija rezultata
plt.figure()
for class_value in np.unique(y):
    mask = y_test == class_value
    plt.scatter(X_test[mask, 0], X_test[mask, 1], label=class_names[class_value], alpha=0.6)
plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('KNN klasifikacija - testni podaci')
plt.legend()
plt.show()
