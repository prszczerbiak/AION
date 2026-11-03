import time

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = load_digits(return_X_y=True)
X = X / 16.0  # pixels 0-16 -> 0-1
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Network 64 -> 16 -> 10 (ReLU hidden layer, softmax output, Adam, backpropagation)
model = MLPClassifier(hidden_layer_sizes=(16,), activation="relu", solver="adam",
                      learning_rate_init=0.01, batch_size=64, max_iter=300,
                      random_state=42)

start = time.time()
model.fit(X_train, y_train)

print(f"Time:           {time.time() - start:.1f} s")
print(f"Train accuracy: {model.score(X_train, y_train):.4f}")
print(f"Test accuracy:  {model.score(X_test, y_test):.4f}")
print(f"Parameters:     {sum(w.size for w in model.coefs_ + model.intercepts_)}")
