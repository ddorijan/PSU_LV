import numpy as np
from tensorflow import keras
from tensorflow.python.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa



# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = Sequential()
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy', optimizer='sgd',metrics=['accuracy'])


# TODO: provedi treniranje mreze pomocu .fit()
model.fit(x_train, y_train, epochs=25, batch_size=32)


# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
loss_and_metrics = model.evaluate(x_test, y_test)


# TODO: Prikazite matricu zabune na skupu podataka za testiranje
classes = model.predict(x_test)


# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala


