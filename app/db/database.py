from pymongo import MongoClient

from app.settings.mongo_config import DB_URL
from app.db.data import menu, QUINOA_STIR_FRY, BUDDHA_BOWL, LENTIL_CURRY

client = MongoClient(DB_URL)

db = client['restaurant']
menu_collection = db['menu']

def init_db():
    menu_collection.drop()
    menu_collection.insert_many([
        menu[BUDDHA_BOWL],
        menu[QUINOA_STIR_FRY],
        menu[LENTIL_CURRY]
    ])