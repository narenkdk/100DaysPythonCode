#Day 63: CRUD application

#Build a basic CRUD (Create, Read, Update, Delete) application.

from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRUD App</title>
    </head>
    <body>
        <h1>Simple CRUD App</h1>
        <input type="text" id="itemInput" placeholder="Enter item name">
        <button onclick="createItem()">Add Item</button>
        <ul id="itemList"></ul>

        <script>
            async function fetchItems() {
                const response = await fetch('/items');
                const items = await response.json();
                document.getElementById('itemList').innerHTML = items.map(item =>
                    `<li>${item.name} 
                        <button onclick="deleteItem(${item.id})">Delete</button>
                        <button onclick="updateItem(${item.id})">Edit</button>
                    </li>`
                ).join('');
            }

            async function createItem() {
                const name = document.getElementById('itemInput').value;
                await fetch('/items', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name })
                });
                fetchItems();
            }

            async function deleteItem(id) {
                await fetch(`/items/${id}`, { method: 'DELETE' });
                fetchItems();
            }

            async function updateItem(id) {
                const newName = prompt("Enter new name:");
                if (newName) {
                    await fetch(`/items/${id}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name: newName })
                    });
                    fetchItems();
                }
            }

            fetchItems();
        </script>
    </body>
    </html>
    """)

@app.route('/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'POST':
        data = request.json
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item created successfully!'})
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@app.route('/items/<int:id>', methods=['PUT', 'DELETE'])
def modify_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    if request.method == 'PUT':
        data = request.json
        item.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Item updated successfully!'})

    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
