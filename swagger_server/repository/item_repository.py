from swagger_server.resources.postgres_db import PostgresClient
from swagger_server.models.item_model import Item

class ItemRepository():

    def create(self, body: Item):
        with PostgresClient() as client:
            response = client.execute_insert('"ITEM"',body)
        return response 
    
    def get_by_id(self, item_id):
        # Adujunta codigo
        with PostgresClient() as client:
            response = client.execute_query('SELECT * FROM "ITEM" WHERE ID=' + str(item_id))
            return response
        ############################

    def update(self, item_id, item_cantidad):
        # Adujunta codigo
        with PostgresClient() as client:
            # Obtengo el registro por medio del id
            val_item = self.get_by_id(item_id)
            # Obtengo el registro por medio de sus posiciones para obtener el stock
            val_item_stock=val_item[0]["stock"]
            # Resto el valor obtenido del stock con la cantidad a comprar
            item_stock = int(val_item_stock - item_cantidad)
            response = client.execute_update('"ITEM"', val_item, 'id = ' + str(item_id), 'stock = ' + str(item_stock))
            return response
        ############################
        
    def get_paginated(self, page, size, name):
        # Adujunta codigo
        with PostgresClient() as client:
            table = '"ITEM"'
            query = f"SELECT * FROM {table} WHERE name like '%{name}%'"
            response = client.execute_query_paginated(query, page, size)
            return response
        ############################