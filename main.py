from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais
tasks = [
    {"id": 1, "details": "Estudar ", "status": "pendente"},
    {"id": 2, "details": "Revisar versionamento de APIs", "status": "concluída"}
]

# Endpoints da versão 1

@app.route('/api/v2/tasks', methods=['GET'])
def get_tasks_v2():
    return jsonify(tasks), 200

@app.route('/api/v2/tasks', methods=['POST'])
def create_task_v2():
    data = request.get_json()
    if not data or 'description' not in data or 'status' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "description": data['description'],
        "status": data['status']
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/v2/tasks/<int:task_id>', methods=['PUT'])
def update_task_v2(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if 'description' in data:
        task['description'] = data['description']
    if 'status' in data:
        task['status'] = data['status']

    return jsonify(task), 200

# Inicialização do servidor
if __name__ == '__main__':
    app.run(debug=True)
