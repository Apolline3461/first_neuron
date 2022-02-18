import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score

X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=0)
y = y.reshape((y.shape[0], 1))

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

plt.scatter(X[:,0], X[:, 1], c=y, cmap='summer')
plt.show()

def initialisation(X):
    W = np.array([X * [0]]).reshape(2,1)
    b = np.array([X])
    return (W, b)

W, b = initialisation(2)
print(W.shape)
print(b.shape)
