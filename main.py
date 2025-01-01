from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# In-memory storage for user data
user_data = {}

# Pydantic model for user input
class UserInput(BaseModel):
    name: str
    age: int

# Route to display all user data
@app.get("/")
def read_root():
    return {"users": user_data}

# Route to add or update user data
@app.post("/users/{user_id}")
def add_or_update_user(user_id: int, user: UserInput):
    user_data[user_id] = {"name": user.name, "age": user.age}
    return {"message": "User added/updated", "user_id": user_id, "user_data": user_data[user_id]}

# Route to get specific user data
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "user_data": user_data[user_id]}

# Route to delete user data
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in user_data:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = user_data.pop(user_id)
    return {"message": "User deleted", "deleted_user": deleted_user}