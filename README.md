# Simple Calculator API

A simple calculator API built with Flask and Flask-RESTful that performs basic arithmetic operations. This project is dockerized for easy deployment.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.x (for local development)

### Installation

#### Local Development

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/simple_calculator.git
    cd simple_calculator
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python -m flask run
    ```

#### Docker

1. Build and run the Docker container:
    ```bash
    docker build -t simple_calculator .
    docker run -p 5000:5000 simple_calculator
    ```

   Or, use Docker Compose:
    ```bash
    docker-compose up
    ```

## API Endpoints

### POST /calculate/<string:operation>

Perform a calculation with `x` and `y` based on the `operation` parameter (`add`, `subt`, `multiply`, `divide`).

- **Request Example**:
    ```json
    {
      "x": 10,
      "y": 5
    }
    ```

- **Response**:
  - **Success**: `{"message": result, "Status Code": 200}`
  - **Error**:
    - Missing parameters: `{"message": "Missing parameters", "Status Code": 400}`
    - Invalid data type: `{"message": "Invalid data type", "Status Code": 400}`
    - Invalid operation: `{"message": "Invalid operation", "Status Code": 400}`
    - Division by zero: `{"Message": "Division by zero", "Status Code": 400}`
    - Internal server error: `{"Message": "Internal server error", "Status Code": 500, "Error": str(e)}`
