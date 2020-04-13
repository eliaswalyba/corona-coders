class NeuralNetwork:

    def __init__(self):
        self.layers = []
        self.loss_fn = None
        self.loss_dfn = None

    def add(self, layer):
        self.layers.append(layer)

    def use(self, loss_fn, loss_dfn):
        self.loss_fn = loss_fn
        self.loss_dfn = loss_dfn
    
    def predict(self, input_data):
        sample = len(input_data)
        result = []

        for i in range(sample):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward(output)
            result.append(output)
        
        return result

    def fit(self, x_train, y_train, epochs, learning_rate):
        samples = len(x_train)

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward(output)
                err += self.loss_fn(y_train[j], output)

                error = self.loss_dfn(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward(error, learning_rate)

            err /= samples
            print('epoch %d/%d   error=%f' % (i+1, epochs, err))