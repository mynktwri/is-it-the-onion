import numpy as np
import pandas as pd
import os
import keras
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()

from sklearn.model_selection import train_test_split

here = os.path.dirname(os.path.abspath(__file__))

onion_keras = np.load(os.path.join(here, 'onion_keras_data.npy'))
notonion_keras = np.load(os.path.join(here, 'notonion_keras_data.npy'))
print(notonion_keras.shape)
print(onion_keras.shape)
onion_target = np.ones(966,)
notonion_target = np.zeros(966,)
X = np.concatenate((onion_keras,notonion_keras))#(1932, 40, 319)
Y = np.concatenate((onion_target,notonion_target))#(1932,)
print(X.shape)
print(Y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)



# input shape is (n, 40, 319)
from keras import layers

# A integer input for vocab indices.
inputs = keras.Input(shape=(40, 319), dtype="float32")

# Conv1D + global max pooling
# x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
# x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
x = layers.GlobalAveragePooling1D()(inputs)

# We add a vanilla hidden layer:
x = layers.Dense(64, activation="relu")(x)
x = layers.Dropout(0.3)(x)


# We project onto a single unit output layer, and squash it with a sigmoid:
predictions = layers.Dense(1, activation="sigmoid", name="predictions")(x)

model = keras.Model(inputs, predictions)

# Compile the model with binary crossentropy loss and an adam optimizer.
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(X_train, y_train, validation_split=0.2, shuffle=False, epochs=15, batch_size=50)

loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
print("Testing Accuracy:  {:.4f}".format(accuracy))
plot_history(history)