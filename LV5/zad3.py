import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay

df = pd.read_csv("occupancy_processed.csv")

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:\n", conf_matrix)


accuracy = accuracy_score(y_test, y_pred)
print("Točnost modela:", accuracy)

print("Izvještaj klasifikacije:\n", classification_report(
    y_test, y_pred, target_names=['Slobodna', 'Zauzeta']))


plt.figure(figsize=(12, 8))
plot_tree(tree, filled=True)
plt.show()


cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,  display_labels=['Class  0',
                                                                    'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()