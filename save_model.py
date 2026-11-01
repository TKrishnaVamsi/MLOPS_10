import joblib
import os
from model import train_model

os.makedirs("artifacts", exist_ok=True)

model = train_model()

joblib.dump(model, "artifacts/model.pkl")

print("Model trained and saved successfully!")