from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Function to load model and scaler
def load_artifacts(model_path: str, scaler_path: str):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

# Load the trained model and scaler
model, scaler = load_artifacts("model.joblib", "scaler.joblib")

# Define a Pydantic model for input validation
class CustomerInput(BaseModel):
    age: int
    suburb_code: int
    salary: int

# Create a FastAPI instance
app = FastAPI()

# Inference endpoint
@app.post("/predict")
def predict_class(customer: CustomerInput):
    # Prepare the input data
    input_data = np.array([[customer.age, customer.suburb_code, customer.salary]])
    
    # Standardize the input data
    input_scaled = scaler.transform(input_data)
    
    # Make a prediction
    prediction = model.predict(input_scaled)
    
    # Map the prediction to a class label
    if prediction < 0.5:
        class_label = "Poor"
    elif prediction < 1.5:
        class_label = "Middle Class"
    else:
        class_label = "High Class"
    
    return {"prediction": class_label}