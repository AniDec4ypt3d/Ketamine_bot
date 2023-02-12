import pymongo





import os
import sys
from typing import Any
from motor import motor_asyncio
from ..core.logger import log
# client = pymongo.MongoClient('mongodb+srv://Ani:s4ZxlUYnolSPaMI3@cluster0.2sfbj.mongodb.net/?retryWrites=true&w=majority',serverSelectionTimeoutMS=5000)

# db = client.bot['main']



class MongoDB(motor_asyncio.AsyncIOMotorClient):
    
    def __init__(self,
                url:str = None,
                database_name: str = 'bot',
                serverSelectionTimeoutMS:int = 5000,
                ):
        try:
            super().__init__("mongo url",serverSelectionTimeoutMS=5000)
            self.db = self[database_name]
        except Exception as er:
            log.exception(er)
            sys.exit(1)


    async def insert_one(self,database_name, dict) -> bool:
        """Insert Document."""
        if await self.db[database_name].insert_one(dict):
            return True
        else:
            return False
    
    async def find_all(self, db_name, dict):
        find = await self.db[db_name].find(dict)
        return find
    
    async def __call__(self, *args: Any, **kwds: Any) -> Any:
        return await self.db[args[0]](*args, **kwds)
    
    async def find_one(self, database_name, dict):
        """Find Document and return it."""
        if isinstance(dict,str or int):
            find = await self.db[database_name].find_one({'_id': dict})
            return find if find else False
        else:
            _ = await self.db[database_name].find_one(dict)
            return _ if _ else False
    
    async def delete(self, database_name, dict) -> bool:
        """Delete Document."""
        if await self.db[database_name].delete_one(dict):
            return True
        else:
            return False

    async def update_one(self, database_name, x , y):
        """Update Document."""
        if await self.db[database_name].update_one(x, y):
            return True
        else:
            return False

    async def get_count(self, db_name ,*args, **kwargs):
        x = await self.db[db_name].count_documents({})
        return x if x else False
    