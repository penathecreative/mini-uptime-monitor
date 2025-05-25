from flask import Blueprint, request, jsonify
import json

main = Blueprint('main', __name__)
DATA_FILE = "data/sites.json"

@main.route('/add', methods=['POST'])
def add_site():
    url = request.json.get("url")
    if not url:
        return {"error": "Missing URL"}, 400

    with open(DATA_FILE, "r+") as f:
        data = json.load(f)
        if url not in data:
            data[url] = {"status": "unknown"}
            f.seek(0)
            json.dump(data, f, indent=4)
    return {"message": f"{url} added"}, 200

@main.route('/status')
def get_status():
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        print(f"[ERROR in /status]: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
