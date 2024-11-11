import numpy as np

class SimpleNN:
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.random.rand(2, 1)
        self.bias = np.random.rand(1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, X, y):
        for _ in range(self.epochs):

            weighted_sum = np.dot(X, self.weights) + self.bias
            prediction = self.sigmoid(weighted_sum)


            error = y - prediction
            adjustments = error * self.sigmoid_derivative(prediction)

 
            self.weights += np.dot(X.T, adjustments) * self.learning_rate 
            self.bias += np.sum(adjustments) * self.learning_rate

    def predict(self, X):
        return self.sigmoid(np.dot(X, self.weights) + self.bias) > 0.5

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([[0], [0], [0], [1]])  
y_or = np.array([[0], [1], [1], [1]]) 

nn_and = SimpleNN()
nn_and.train(X, y_and)
print("AND Gate Predictions:", nn_and.predict(X))

nn_or = SimpleNN()
nn_or.train(X, y_or)
print("OR Gate Predictions:", nn_or.predict(X))
