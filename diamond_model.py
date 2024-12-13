import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load and prepare the data
data = pd.read_csv("diamonds.csv")
data = data.drop("Unnamed: 0", axis=1)
data["cut"] = data["cut"].map({"Ideal": 1, "Premium": 2, "Good": 3, "Very Good": 4, "Fair": 5})
data["size"] = data["x"] * data["y"] * data["z"]

# Features and target
x = np.array(data[["carat", "cut", "size"]])
y = np.array(data["price"])

# Split the data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(xtrain, ytrain)

def predict_price(carat, cut, size):
    features = np.array([[carat, cut, size]])
    return model.predict(features)[0]
