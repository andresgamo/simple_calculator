from flask import Flask, jsonify
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app)

class Operation:
    def execute(self, x: float, y: float) -> float:
        """Execute the operation."""
        raise NotImplementedError

class Add(Operation):
    def execute(self, x: float, y: float) -> float:
        return x + y

class Subtract(Operation):
    def execute(self, x: float, y: float) -> float:
        return x - y

class Multiply(Operation):
    def execute(self, x: float, y: float) -> float:
        return x * y

class Divide(Operation):
    def execute(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Division by zero")
        return x / y

class OperationFactory:
    def get_operation(self, operation: str) -> Operation:
        operations = {
            "add": Add(),
            "subt": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
        }
        return operations.get(operation)

class CalculatorAPI(Resource):
    def __init__(self) -> None:
        self.operation_factory = OperationFactory()

    def post(self, operation: str):
        """Handle the POST request for a calculation."""
        posted_data = request.get_json()
        x = posted_data.get("x")
        y = posted_data.get("y")

        if x is None or y is None:
            return jsonify({"message": "Missing parameters", "Status Code": 400})

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return jsonify({"message": "Invalid data type", "Status Code": 400})

        operation_instance = self.operation_factory.get_operation(operation)
        if operation_instance is None:
            return jsonify({"message": "Invalid operation", "Status Code": 400})

        try:
            result = operation_instance.execute(x, y)
        except ValueError as e:
            return jsonify({"Message": str(e), "Status Code": 400})
        except Exception as e:
            return jsonify({"Message": "Internal server error", "Status Code": 500, "Error": str(e)})

        return jsonify({"message": result, "Status Code": 200})

@app.route("/")
def index():
    return "Time to calculate"

api.add_resource(CalculatorAPI, "/calculate/<string:operation>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")