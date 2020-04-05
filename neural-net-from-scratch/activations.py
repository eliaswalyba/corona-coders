import numpy as np

def sigmoid(x):
    def f(x):
        s = 1 / 1 + np.exp(-x)
        return s
    
    def df(x):
        ds = sigmoid(x) * (1 - sigmoid(x))
        return ds

    return f, df