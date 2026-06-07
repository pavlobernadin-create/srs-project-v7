# app.py
from flask import Flask, jsonify, request
from models import Item

app = Flask(__name__)

# Початкові дані
items = [Item(1, "Тестове завдання", "Зробити лабу").to_dict()]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    new_data = request.json
    new_item = Item(len(items) + 1, new_data['name'], new_data['description'])
    items.append(new_item.to_dict())
    return jsonify(new_item.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)