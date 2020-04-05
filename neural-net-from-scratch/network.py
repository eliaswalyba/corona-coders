import numpy as np

class NeuralNetwork:

    def __init__(self, n_input, n_hidden, n_output, activation, lr):
        self.n_input, self.n_hidden, self.n_output = n_input, n_hidden, n_output
        self.activation = {
            'f': np.vectorize(activation.get('f')),
            'df': np.vectorize(activation.get('df'))
        }
        self.lr = lr
        self.weights = {
            'i -> h': np.random.rand(self.n_hidden, self.n_input),
            'h -> o': np.random.rand(self.n_output, self.hidden)
        }
        self.biases = {
            'h': np.random.rand(self.n_hidden, 1),
            'o': np.random.rand(self.n_output, 1)
        }

    def train(self, x, y):
        X = np.array(x).reshape(-1, 1)
        Y = np.array(y).reshape(-1, 1)

        # feed forward
        H = self.activation.get('f')((self.weights.get('i -> h') * X + self.biases.get('h')))
        O = self.activation.get('f')((self.weights.get('h -> o') * H + self.biases.get('o')))

        # Back propagation
        OE = O - Y # a modifier

        OG = self.activation.get('df')((O)) * OE * self.lr
        self.weights['h -> o'] += OG * H.T
        self.biases['o'] += OG

        HE = self.weights.get('h -> o').T * OE
        HG = self.activation.get('df')((H)) * HE * self.lr
        self.weights['i -> h'] += HG * X.T
        self.biases['h'] += HG

    def predict(self):
        pass