import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Generate dummy data
np.random.seed(42)
n_samples = 1000

# Features: age, suburb_code, salary
age = np.random.randint(18, 65, size=n_samples)
suburb_code = np.random.randint(1, 10, size=n_samples)
salary = np.random.randint(20000, 150000, size=n_samples)

# Target: class (0 = poor, 1 = middle class, 2 = high class)
target = np.zeros(n_samples)
target[(salary >= 30000) & (salary < 80000)] = 1  # Middle class
target[salary >= 80000] = 2  # High class

# Combine features into a single array
X = np.column_stack((age, suburb_code, salary))

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_scaled, target)

# Save the model and scaler as artifacts
joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("Model and scaler saved as artifacts.")