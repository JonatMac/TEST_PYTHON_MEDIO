from typing import List
from swagger_server.utils.logging import log as logging
from swagger_server.repository.item_repository import ItemRepository
from swagger_server.models.item_model import Item

from pydantic import parse_obj_as

class ItemUseCase():

    def __init__(self):
        log = logging()
        self.item_repository = ItemRepository()
        self.log = log

    def save(self, request):
        data = self.item_repository.create(request.dict())
        response = parse_obj_as(Item, data)
        return response
    
    def get_item(self, item_id):
        # Adujunta codigo
        response = self.item_repository.get_by_id(item_id)
        items = None
        if response:
            items = parse_obj_as(Item, response[0])
        return items
        ############################
    
    def get_all(self):
        response = self.item_repository.get_all()
        items = parse_obj_as(List[Item], response)
        return items
    
    def update(self, item_id, item_cantidad):
        # Adujunta codigo
        response = self.item_repository.update(item_id, item_cantidad)
        items = parse_obj_as(Item, response)
        return items
        ############################

    def get_paginated(self, page, size, name):
        # Adujunta codigo
        response = self.item_repository.get_paginated(page, size, name)
        items = parse_obj_as(List[Item], response)
        return items
        ############################