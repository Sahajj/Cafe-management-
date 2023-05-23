from flask import Flask, request

app = Flask(__name__)


items = [
        {
            "name" : "Green Apple Mojito",
            "price": 160
        },
        {
            "name" : "Momos",
            "price": 60
        }
]

@app.get('/items')
def get_items():
    return {"items":items}

@app.get('/item')
def get_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
            return item
    return {'message': "Recoed doesn't exisit"}, 404

@app.post('/item')
def add_item():
    request_data = request.get_json()
    items.append(request_data)
    return {"message":"item added successfully"}, 201

@app.put('/item')
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name'] == request_data['name']:
            item['price'] = request_data['price']
            return {"message":"item updated successfully"}
    return {"message":"Given record Doesn't exist"}, 404


@app.delete('/item')
def delete_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
            items.remove(item)
            return {'message' : 'Item delete successfully'}
    return {'message': "Recoed doesn't exisit"}, 404
