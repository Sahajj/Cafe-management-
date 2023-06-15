from flask import Flask, request
import uuid
from db import items
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemGetSchema , SuccessMessageSchema, ItemQuerySchema, ItemOptionalQuerySchmea

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item")
class Item(MethodView):

    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptionalQuerySchmea, location="query")
    def get(self, args):
        id = args.get('id')
        if id is None:
            return items
        for item in items:
            if item['id'] == id:
                return [item]
        abort(404 ,message = "Recoed doesn't exisit")

    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data, args):
        id = args.get('id')
        for item in items:
            if item['id'] == id:
                item['item']['name'] = request_data['name']
                item['item']['price'] = request_data['price']  
                return {"message":"item updated successfully"}, 200
        abort(404 ,message = "Not found")

    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        item = {
            'id':uuid.uuid4().hex,
            'item' : {
                "name" : request_data["name"],
                "price" : request_data["price"]
                 }
            }
        items.append(item)
        return {"message":"item added successfully"}, 201

    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        for item in items:
                if item['id'] == id:
                    items.remove(item)
                    return {'message' : 'Item delete successfully'}
 
        abort(404 ,message = "Recoed doesn't exisit")