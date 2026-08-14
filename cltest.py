from flask  import Flask, jsonify, request
import json

app = Flask(__name__)

def load_shipments():
    try:
        with open("shipments.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_shipments(shipments):
    with open("shipments.json", "w") as f:
        json.dump(shipments, f)


        

@app.route("/shipments")
def shipments():
    return jsonify(load_shipments())

@app.route("/shipments", methods=["POST"])
def create_shipment():
    data = request.get_json()
    if not data:
      return jsonify({"error": "No data sent"}), 400
    if not data.get("destination"):
      return jsonify({"error": "Destination required"}), 400
    if not data.get("weight") or data.get("weight") <= 0:
      return jsonify({"error": "Valid weight required"}), 400
    shipments = load_shipments()
    shipments.append(data)
    save_shipments(shipments)

    return jsonify({"message": "Shipment created successfully"}), 201

shipments = load_shipments()
new_shipment = {
    "id": len(shipments) + 1,
    "destination": data.get("destination"),
    "weight": data.get("weight"),
    "status": "pending"
}
shipments.append(new_shipment)

if __name__ == "__main__":
    app.run(debug=True)