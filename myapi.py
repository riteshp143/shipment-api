from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.json.sort_keys = False

FILE_NAME = "shipments.json"

def load_shipments():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_shipments(shipments):
    with open(FILE_NAME, "w") as f:
        json.dump(shipments, f, indent=4)

shipments = load_shipments()

@app.route("/shipments", methods=["GET"])
def get_shipments():
    shipments = load_shipments()
    return jsonify(shipments)

@app.route("/shipments/<int:shipment_id>", methods=["GET"])
def get_shipment(shipment_id):
    shipments = load_shipments()
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return jsonify(shipment)
    return jsonify({"error": "Shipment not found"}), 404

@app.route("/shipments", methods=["POST"])
def create_shipment():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    destination = data.get("destination")
    weight = data.get("weight")
    if not destination:
        return jsonify({"error": "Destination is required"}), 400
    if not weight or weight <= 0:
        return jsonify({"error": "Weight must be a positive number"}), 400
    shipments = load_shipments()
    shipment = {
        "id": len(shipments) + 1,
        "destination": destination,
        "weight": weight,
        "status": "pending"
    }
    shipments.append(shipment)
    save_shipments(shipments)
    return jsonify({"message": "Shipment created!", "shipment": shipment}), 201

@app.route("/shipments/<int:shipment_id>", methods=["PUT"])
def update_shipment(shipment_id):
    data = request.get_json()
    shipments = load_shipments()
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipment["destination"] = data.get("destination", shipment["destination"])
            shipment["weight"] = data.get("weight", shipment["weight"])
            shipment["status"] = data.get("status", shipment["status"])
            save_shipments(shipments)
            return jsonify({"message": "Shipment updated!", "shipment": shipment})
    return jsonify({"error": "Shipment not found"}), 404

@app.route("/shipments/<int:shipment_id>", methods=["DELETE"])
def delete_shipment(shipment_id):
    shipments = load_shipments()
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipments.remove(shipment)
            save_shipments(shipments)
            return jsonify({"message": "Shipment deleted!"})
    return jsonify({"error": "Shipment not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)