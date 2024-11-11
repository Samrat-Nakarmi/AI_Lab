import numpy as np

class BackpropagationNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5, epochs=10000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_hidden = np.random.rand(hidden_size)
        self.bias_output = np.random.rand(output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, X, y):
        for _ in range(self.epochs):
            hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
            hidden_layer_output = self.sigmoid(hidden_layer_input)
            output_layer_input = np.dot(hidden_layer_output, self.weights_hidden_output) + self.bias_output
            prediction = self.sigmoid(output_layer_input)

            error_output_layer = y - prediction
            delta_output_layer = error_output_layer * self.sigmoid_derivative(prediction)

            error_hidden_layer = delta_output_layer.dot(self.weights_hidden_output.T)
            delta_hidden_layer = error_hidden_layer * self.sigmoid_derivative(hidden_layer_output)

            self.weights_hidden_output += hidden_layer_output.T.dot(delta_output_layer) * self.learning_rate
            self.weights_input_hidden += X.T.dot(delta_hidden_layer) * self.learning_rate
            self.bias_output += np.sum(delta_output_layer, axis=0) * self.learning_rate
            self.bias_hidden += np.sum(delta_hidden_layer, axis=0) * self.learning_rate

    def predict(self, X):
        hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        hidden_layer_output = self.sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, self.weights_hidden_output) + self.bias_output
        prediction = self.sigmoid(output_layer_input)
        return prediction

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

nn = BackpropagationNN(input_size=2, hidden_size=2, output_size=1)
nn.train(X, y)
print("XOR Predictions:", nn.predict(X))
