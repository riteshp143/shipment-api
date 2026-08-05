# Shipment API

A REST API for managing shipments built with Python and Flask.

## What it does

- Add new shipments
- View all shipments
- Find a shipment by ID
- Update shipment details
- Delete a shipment


## Tech stack

- Python
- Flask
- JSON file storage

## How to run

1. Install Flask:
   pip install flask

2. Run the server:
   python myapi.py

3. Test with Postman at:
   http://localhost:5000/shipments

   ## API endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /shipments | Get all shipments |
| GET | /shipments/<id> | Get one shipment |
| POST | /shipments | Add new shipment |
| PUT | /shipments/<id> | Update shipment |
| DELETE | /shipments/<id> | Delete shipment |

## Built by

Ritesh Poojary — transitioning from LCL Export Customer Support 
to Backend Development.