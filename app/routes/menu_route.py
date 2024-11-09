from flask import Blueprint, request, jsonify

from app.rabbit.publish import publish_topic
from app.repository.menu_repository import insert_meal, order_meal
from app.settings.rabbit_config import REST_STOCK_AMOUNT_ROUTING_KEY

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/new', methods=['POST'])
def add_item():
    item = request.json
    inserted_item = insert_meal(item)
    return jsonify({
        **inserted_item,
        '_id': str(inserted_item['_id'])
    }), 201

@menu_blueprint.route('/order/<string:item_name>', methods=['PUT'])
def order_item(item_name):
    item = order_meal(item_name)
    publish_topic(item, REST_STOCK_AMOUNT_ROUTING_KEY)
    return jsonify({ **item, '_id': str(item['_id']) }), 200