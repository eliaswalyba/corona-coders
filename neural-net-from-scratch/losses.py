import numpy as np

def mse(y, y_hat):
    return np.mean(np.power(y - y_hat, 2))

def d_mse(y, y_hat):
    return 2*(y_hat - y)/y.size