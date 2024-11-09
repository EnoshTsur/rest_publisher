from app.db.database import menu_collection

def insert_meal(item):
    menu_collection.insert_one(item)
    return item

def order_meal(item_name):
    menu_filter = { 'name': item_name }
    item = menu_collection.find_one(menu_filter)
    if not item:
        return

    def decrease_stock(ingredient):
        return {
            **ingredient,
            'stock': ingredient['stock'] - ingredient['amount']
        }

    new_ingredients = {
        key: decrease_stock(value)
        for key, value in dict.items(item['ingredients'])
    }

    menu_collection.update_one(
        menu_filter,
        {'$set': { 'ingredients': new_ingredients }}
    )

    return menu_collection.find_one(menu_filter)
