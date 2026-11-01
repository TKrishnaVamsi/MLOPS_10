from sklearn.linear_model import LinearRegression

def train_model():
    X = [[1], [2], [3], [4], [5]]
    y = [2, 4, 6, 8, 10]

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict(model, value):
    return model.predict([[value]])[0]