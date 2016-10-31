import sys, pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.svm import SVR
inp = float(sys.stdin.readline())

data = pd.read_csv("trainingdata.txt",header=None,names=["time","battery"])
print data.head()
train_X, test_X, train_y, test_y = data["time"][:-20], data["time"][-20:], data["battery"][:-20],data["battery"][-20:]

regr = SVR(C=1.0, epsilon=0.2)# linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(train_X.reshape(-1,1),train_y)

print regr.predict(inp)
