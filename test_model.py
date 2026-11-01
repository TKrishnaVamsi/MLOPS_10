from model import train_model, predict

def test_model_training():
    model = train_model()
    assert model is not None

def test_model_prediction():
    model = train_model()
    result = predict(model, 6)

    assert abs(result - 12) < 0.01