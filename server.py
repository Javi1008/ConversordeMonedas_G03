# server.py
import json
import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from datetime import datetime
# Ya no necesitamos 'random' si usamos un ID secuencial simple.

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "db.json")

app = Flask(__name__)
CORS(app)  # habilita CORS

# -------------------------
# Helpers simples para leer/escribir db.json
# -------------------------
def read_db():
    if not os.path.exists(DB_PATH):
        # El archivo NO existe. Inicializar db con el contador 'last_id' en 0.
        data = {"users": [], "last_id": 0}
        write_db(data)
        return data
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            db_data = json.load(f)
            # Asegurar que 'last_id' existe incluso si el archivo ya existía
            if 'last_id' not in db_data:
                db_data['last_id'] = 0
            return db_data
        except json.JSONDecodeError:
            # Si el archivo está corrupto, reiniciar mínimo
            data = {"users": [], "last_id": 0}
            write_db(data)
            return data

def write_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ----------------------------------
# FUNCIONES DE ID (Refactorizadas)
# ----------------------------------
def _format_id(id_num):
    """Función auxiliar para formatear el número con el prefijo 'User_'."""
    ID_LENGTH = 7
    ID_PREFIX = "User_"
    # Rellenar con ceros a la izquierda
    numeric_part = str(id_num).zfill(ID_LENGTH)
    return ID_PREFIX + numeric_part

def generate_id(db):
    """Genera el siguiente ID único y actualiza el contador global en db."""
    MAX_ID = 9999999
    
    # Obtener el último ID usado y añadir 1.
    next_id_num = db.get("last_id", 0) + 1
    
    if next_id_num > MAX_ID:
        raise Exception("Límite de IDs secuenciales (7 dígitos) alcanzado.")
        
    # Guardar el nuevo last_id en la base de datos (en el objeto 'db')
    db["last_id"] = next_id_num

    # Formatear y devolver el ID (e.g., User_0000001)
    return _format_id(next_id_num)


# -------------------------
# Endpoints: Users CRUD
# -------------------------
@app.route("/users", methods=["GET"])
def get_users():
    db = read_db()
    return jsonify(db.get("users", [])), 200

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    db = read_db()
    user = next((u for u in db.get("users", []) if u.get("id") == user_id), None)
    if not user:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "JSON inválido"}), 400
    
    name = payload.get("name") or payload.get("nombre") or payload.get("Name")
    if not name:
        return jsonify({"error": "name es requerido"}), 400

    db = read_db()
    
    try:
        # Generar el nuevo ID, esto también actualiza db["last_id"]
        new_id = generate_id(db)
    except Exception as e:
        return jsonify({"error": str(e)}), 507 
    
    # Crear nuevo objeto usuario
    new_user = {
        "id": new_id, 
        "name": name,
        "email": payload.get("email", ""),
        "prefCurrency": payload.get("prefCurrency", ""),
        "created": datetime.utcnow().isoformat(),
        "historial": payload.get("historial", []) or []
    }
    users = db.get("users", [])
    users.append(new_user)
    db["users"] = users
    
    # Escribir db con el nuevo usuario Y el nuevo last_id
    write_db(db)
    return jsonify(new_user), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "JSON inválido"}), 400
    db = read_db()
    users = db.get("users", [])
    idx = next((i for i,u in enumerate(users) if u.get("id") == user_id), None)
    if idx is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    existing = users[idx]
    merged = { **existing, **payload }
    merged["id"] = existing["id"]
    if "created" not in merged:
        merged["created"] = existing.get("created", datetime.utcnow().isoformat())
    if not isinstance(merged.get("historial", []), list):
        merged["historial"] = existing.get("historial", [])
    users[idx] = merged
    db["users"] = users
    write_db(db)
    return jsonify(merged), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = read_db()
    users = db.get("users", [])
    new_users = [u for u in users if u.get("id") != user_id]
    if len(new_users) == len(users):
        return jsonify({"error": "Usuario no encontrado"}), 404
    db["users"] = new_users
    write_db(db)
    return jsonify({"ok": True}), 200

@app.route("/users/<user_id>/historial", methods=["GET"])
def historial_usuario(user_id):
    db = read_db()
    user = next((u for u in db.get("users", []) if u.get("id") == user_id), None)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.get("historial", [])), 200

# -------------------------
# Iniciar servidor
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)