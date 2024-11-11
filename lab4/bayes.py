from collections import defaultdict
import math

class NaiveBayesClassifier:
    def __init__(self):
        self.class_counts = defaultdict(int)
        self.feature_counts = defaultdict(lambda: defaultdict(int))
        self.total_samples = 0
    
    def train(self, X, y):
        self.total_samples = len(y)
        for features, label in zip(X, y):
            self.class_counts[label] += 1
            for feature, value in features.items():
                self.feature_counts[label][(feature, value)] += 1
    
    def predict(self, X):
        predictions = []
        for features in X:
            max_prob, best_label = -math.inf, None
            for label, count in self.class_counts.items():
                prob = math.log(count / self.total_samples)
                for feature, value in features.items():
                    prob += math.log((self.feature_counts[label].get((feature, value), 0) + 1) /
                                     (count + len(self.feature_counts[label])))
                if prob > max_prob:
                    max_prob, best_label = prob, label
            predictions.append(best_label)
        return predictions

# Example usage:
X_train = [{'feature1': 'sunny', 'feature2': 'hot'},
           {'feature1': 'rainy', 'feature2': 'cool'},
           {'feature1': 'sunny', 'feature2': 'mild'}]
y_train = ['play', 'no play', 'play']

X_test = [{'feature1': 'sunny', 'feature2': 'hot'}]

nb = NaiveBayesClassifier()
nb.train(X_train, y_train)
print("Prediction:", nb.predict(X_test))
