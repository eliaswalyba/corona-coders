import numpy as np

class BaseLayer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input_data):
        raise NotImplementedError

    def backward(self, output_error, lr):
        raise NotImplementedError

class ActivationLayer(BaseLayer):
    def __init__(self, activation_fn, activation_dfn):
        self.activation_fn = activation_fn
        self.activation_dfn = activation_dfn

    def forward(self, input_data):
        self.input = input_data
        self.output = self.activation_fn(self.input)
        return self.output

    def backward(self, output_error, lr):
        return self.activation_dfn(self.input) * output_error


class DenseLayer(BaseLayer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - .5
        self.bias = np.random.rand(1, output_size) - .5

    def forward(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    def backward(self, output_error, lr):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)
        self.weights -= lr * weights_error
        self.bias -= lr * output_error
        return input_error