from fastapi import FastAPI, HTTPException

# Initialize the FastAPI app
app = FastAPI(
    title="My First API",
    description="API built with FastAPI",
    version="1.0.0"
)

# 1. Root Endpoint (GET /)
@app.get("/")
def read_root():
    return {
        "message": "Welcome to my FastAPI application!",
    }


# 2. Path Parameter Endpoint (GET /greet/{name})
@app.get("/greet/{name}")
def greet_user(name: str):
    
    return {
        "greeting": f"Hello, {name.title()}!",
        "message": "Hope you have a great day learning FastAPI!"
    }


# 3. Query Parameter Endpoint (GET /calculate/square)
@app.get("/calculate/square")
def calculate_square(number: int = None):

    # Check if the required query parameter was provided
    if number is None:
        raise HTTPException(
            status_code=400, 
            detail="Missing parameter! Please provide a 'number' query parameter, e.g., /calculate/square?number=5"
        )
    
    return {
        "input_number": number,
        "square": number ** 2
    }