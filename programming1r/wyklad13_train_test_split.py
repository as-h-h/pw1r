import numpy as np


# podział na część treningową i testową "ręcznie"
# pewna wada: jeśli y nie są floatami, nastąpi zmiana typów etykietek/danych
# (wada rozwiąże się na następnym wykładzie)
def train_test_split(X, y, train_size=0.5):
    n = int(train_size * X.shape[0])
    A = np.hstack((X, y.reshape(-1, 1)))
    np.random.shuffle(A)
    X_train = A[:n, :-1]
    X_test = A[n:, :-1]
    y_train = A[:n, -1]
    y_test = A[n:, -1]
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X = np.random.random(size=(10, 2))
    y = np.random.randint(1, 4, 10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)
    print(X)
    print()
    print(y)
    print()
    print(X_train)
    print()
    print(X_test)
    print()
    print(y_train)
    print()
    print(y_test)
