import numpy as np

class LinearRegression:
    def __init__(self):
        self.A = None

    def fit(self, x, y):
        ones = np.ones((x.shape[0], 1))
        X = np.hstack((ones, x))
        self.A = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, x):
        ones = np.ones((x.shape[0], 1))
        x_augmented = np.hstack((ones, x))
        return  x_augmented @ self.A



if __name__ == "__main__":
    n = 50
    x = np.random.uniform(2, 10, n)
    y = 2 * x + 5 + np.random.randn(n)
    
    X = x.reshape(-1, 1) # (n, 1)

    model = LinearRegression()
    model.fit(X, y)
    y_predicted = model.predict(X)
    mse = np.mean((y_predicted - y)**2)
    print(mse)
