import numpy as np

def sigmoid(x):
    s = 1 / 1 + np.exp(-x)
    return s
    
def d_sigmoid(x):
    ds = sigmoid(x) * (1 - sigmoid(x))
    return ds