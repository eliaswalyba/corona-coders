import numpy as np
from network import NeuralNetwork
from layers import DenseLayer, ActivationLayer
from activations import sigmoid, d_sigmoid
from losses import mse, d_mse

x_train = np.array([
    [[0, 0]], 
    [[0, 1]], 
    [[1, 0]], 
    [[1, 1]]
])
y_train = np.array([
    [[0]],
    [[1]],
    [[1]],
    [[0]]
])

model = NeuralNetwork()
model.add(DenseLayer(2, 3))
model.add(ActivationLayer(sigmoid, d_sigmoid))
model.add(DenseLayer(3, 1))
model.add(ActivationLayer(sigmoid, d_sigmoid))

model.use(mse, d_mse)

model.fit(x_train, y_train, epochs=1000, learning_rate=0.1)

y_hat = model.predict(x_train)
print(y_hat)