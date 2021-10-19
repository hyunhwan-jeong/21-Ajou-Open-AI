import numpy as np

train = np.load("train.npz")
test = np.load("test.npz") 
print(list(train.keys()))
print(list(test.keys()))

X_train, y_train = train["X_train"], train["y_train"]
X_test, y_test = test["X_test"], test["y_test"]

print(X_train.shape)
print(np.unique(y_train))

np.savez_compressed("data/X_train.npz", X_train)
np.savez_compressed("data/X_test.npz",  X_test)

np.savez_compressed("data/y_train.npz", y_train)
np.savez_compressed("data/y_test.npz",  y_test)