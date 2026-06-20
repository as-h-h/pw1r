import numpy as np

# Zakładamy, że centroidy są podane wprost
class CentroidClassifier0:
    def __init__(self):
        self.centroids = None
        self.classes_ = None

    def fit0(self, centroids):
        self.centroids = centroids
        return self

    def fit(self, X, y):
        classes = np.unique(y)
        self.classes_ = classes
        self.centroids = np.array([X[y == c].mean(axis=0) for c in classes])
        return self
        
    def predict0(self, X):
        dist2 = np.sum((X[:, None, :] -self.centroids[None, :, :])**2, axis=2)
        return np.argmin(dist2, axis=1)

    def predict(self, X):
        indices = self.predict0(X)
        return self.classes_[indices]