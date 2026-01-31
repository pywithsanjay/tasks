from flask import Flask, render_template,jsonify,request
import json
from users import register_user, login_user, verify_session
from functools import wraps
from datetime import datetime

app= Flask(__name__)

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        session_key = request.headers.get("Session-Key")
        if not session_key:
            return jsonify({"error": "Session key missing"}), 401

        session = verify_session(session_key)
        if not session:
            return jsonify({"error": "Invalid session"}), 403

        return f(*args, **kwargs)
    return wrapper



def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"data": {"task": []}}

data = load_data()


def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


@app.route("/",methods=["GET"])
def home():
    return "Hello World"



@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    user, error = register_user(data["username"], data["password"])

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "User registered", "user": user})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    session_key = login_user(data["username"], data["password"])

    if not session_key:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"session_key": session_key})



@app.route('/tasks', methods=['GET'])
def taskdata():
    return jsonify({'data': data['data']['task']})


from datetime import datetime

@app.route('/api/add/task', methods=['POST'])
@require_auth
def add_task():
    data_from_request = request.get_json()

    if not data_from_request.get("title"):
        return jsonify({"error": "Title is required"}), 400

    created_at = data_from_request.get(
        "created_at",
        datetime.utcnow().isoformat()
    )

    new_task = {
        "id": len(data["data"]["task"]) + 1,
        "title": data_from_request["title"],
        "description": data_from_request.get("description", ""),
        "completed": False,        
        "created_at": created_at,
        "updated_at": None
    }

    data["data"]["task"].append(new_task)
    save_data(data)

    return jsonify({
        "message": "Task created successfully",
        "task": new_task
    }), 201


@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = next((task for task in data['data']['task'] if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'task not found'}), 404
    return jsonify({'data': task})




@app.route('/api/task/update/<int:id>', methods=['PUT'])
@require_auth
def update_task(id):
    task = next((task for task in data['data']['task'] if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data_from_request = request.get_json()

    task['title'] = data_from_request.get('title', task['title'])
    task['description'] = data_from_request.get('description', task['description'])
    task['completed'] = data_from_request.get('completed', task['completed'])

    task['updated_at'] = datetime.utcnow().isoformat()
    save_data(data)

    return jsonify({
        'message': 'Task updated successfully',
        'task': task
    }), 200



@app.route('/api/remove/tasks/<int:id>', methods=['DELETE'])
@require_auth
def delete_person(id):
    task = next((task for task in data['data']['task'] if task['id'] == id), None)
    if id is None:
        return jsonify({'error': 'Person not found'}), 404

    data['data']['task'].remove(task)
    save_data(data)

    return jsonify({'message': 'task deleted', 'task': task})

app.run()