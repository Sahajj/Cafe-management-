from flask import Flask, request
import uuid
from db import items
app = Flask(__name__)

@app.get('/items')
def get_items():
    return {"items":items}

@app.get('/item')
def get_item():
    id = request.args.get('id')
    try :
        return items[id]
    except KeyError:
        return {'message': "Recoed doesn't exisit"}, 404

@app.post('/item')
def add_item():
    request_Data = request.get_json()
    if "name" not in request_Data or "price" not in request_Data:
        return {'message': "Please input name and price must be included in body"}, 400
    items[uuid.uuid4().hex]= request.get_json()
    return {"message":"item added successfully"}, 201

@app.put('/item')
def update_item():
    id = request.args.get('id')
    if id == None:
        return {'message': "Given id not found"}, 404 

    if id in items.keys():
        request_Data = request.get_json()
        if "name" not in request_Data or "price" not in request_Data:
            return {'message': "Please input name and price must be included in body"}, 400 
        items[id] = request.get_json()
        return {"message":"item updated successfully"}, 200
    else :
         return {'message': "Not found"}, 404


@app.delete('/item')
def delete_item():
    id = request.args.get('id')
    if id == None:
        return {'message': "Given id not found"}, 404 
    if id in items.keys():
        del items[id] 
        return {'message' : 'Item delete successfully'}
    return {'message': "Recoed doesn't exisit"}, 404

