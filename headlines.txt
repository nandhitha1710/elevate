from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}

# --------------------------
# 1) GET all users
# --------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# --------------------------
# 2) GET single user by ID
# --------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"message": "User not found"}), 404

# --------------------------
# 3) POST — Add a new user
# --------------------------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get("id")
    
    if user_id in users:
        return jsonify({"message": "User already exists"}), 400
    
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User added successfully"}), 201

# --------------------------
# 4) PUT — Update user
# --------------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify({"message": "User updated successfully"})

# --------------------------
# 5) DELETE — Remove user
# --------------------------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
