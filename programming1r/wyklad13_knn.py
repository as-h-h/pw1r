import numpy as np

class KNNClassifier:
    def __init__(self, k):
        self.k = k
        self.data = None
        self.labels = None
        
    def fit(self, X, y):
        self.data = X
        self.labels = y
        return self

    def predict(self, X):
        y = []
        # a bez pętli?
        for p in X:
            dist_sq = np.sum((self.data - p)**2, axis=1)
            closest_idx = np.argpartition(dist_sq, self.k)[:self.k]
            closest = self.data[closest_idx]
            values, counts = np.unique(self.labels[closest_idx], return_counts=True)
            y.append(values[np.argmax(counts)])
        return np.array(y)


            
