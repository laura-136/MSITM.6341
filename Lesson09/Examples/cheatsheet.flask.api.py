# Flask API Cheat Sheet
# Instructor: Dennis Wang
# Course: MSITM 6341 - Python Programming
# Topic: Building APIs with Flask

"""
SECTION 1: Getting Started with Flask API
"""
# 1. Install Flask if you haven’t already:
#    pip install flask

# 2. Basic folder structure for API project:
#    project_folder/
#    ├── app.py
#    ├── requirements.txt
#    └── (optional) /static, /templates, /routes, /models

"""
SECTION 2: Basic API with Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API"})

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"greeting": "Hello, world!"})

if __name__ == '__main__':
    app.run(debug=True)


"""
SECTION 3: API Endpoints with Query Parameters and JSON Input
"""
@app.route('/api/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    result = data.get('a', 0) + data.get('b', 0)
    return jsonify({"sum": result})


"""
SECTION 4: Using Path Parameters
"""
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # Simulate lookup
    return jsonify({"user_id": user_id, "name": f"User_{user_id}"})


"""
SECTION 5: HTTP Methods and RESTful Style
"""
# Sample CRUD routes for a resource called "items"
items = []

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify({"message": "Item created", "item": data}), 201

@app.route('/api/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    if 0 <= index < len(items):
        items[index] = data
        return jsonify({"message": "Item updated", "item": data})
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(items):
        deleted = items.pop(index)
        return jsonify({"message": "Item deleted", "item": deleted})
    return jsonify({"error": "Item not found"}), 404


"""
SECTION 6: Error Handling
"""
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


"""
SECTION 7: Using Postman or curl for Testing
"""
# GET request (browser or curl):
# curl http://localhost:5000/api/hello

# GET with query param:
# curl "http://localhost:5000/api/greet?name=Dennis"

# POST request with JSON:
# curl -X POST -H "Content-Type: application/json" -d '{"a": 5, "b": 7}' http://localhost:5000/api/sum


"""
SECTION 8: Structuring a Larger Flask API Project
"""
# Recommended folder structure for maintainability:
# ├── app.py
# ├── routes/
# │   ├── __init__.py
# │   ├── users.py
# │   └── items.py
# ├── models/
# │   └── schemas.py
# ├── utils/
# └── config.py

# In app.py:
# from flask import Flask
# from routes.users import user_bp
# from routes.items import item_bp
#
# app = Flask(__name__)
# app.register_blueprint(user_bp)
# app.register_blueprint(item_bp)


"""
SECTION 9: Flask Extensions for APIs
"""
# Flask-RESTful: Build class-based APIs quickly
# Flask-CORS: Handle cross-origin requests
# Flask-JWT-Extended: Secure APIs with JWT tokens
# Flask-SQLAlchemy: Database ORM integration
# Flask-Marshmallow: Serialization & validation


"""
SECTION 10: Next Steps
"""
# ✅ Add authentication (token-based or session-based)
# ✅ Connect to a database (SQLite, PostgreSQL)
# ✅ Use Blueprints for modular structure
# ✅ Add documentation with Swagger or Postman collections
# ✅ Deploy using Gunicorn + Heroku, Render, or AWS
