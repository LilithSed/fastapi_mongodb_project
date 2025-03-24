# -*- coding: utf-8 -*-
import time

from fastapi.logger import logger
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ServerSelectionTimeoutError

from main.api.classes.singleton import Singleton
from main.api.config.settings import settings



class MongoDBConnection(metaclass=Singleton):
    """
    A helper class to manage MongoDB connections and interactions.
    """

    def __init__(self):
        self.client = self.connect_to_mongodb()

    def connect_to_mongodb(self):
        """
        Establishes a connection to MongoDB, with retries every 3 seconds in case of a
        ServerSelectionTimeoutError.

        Returns:
            MongoClient: An instance of the MongoClient connected to the specified MongoDB server.

        Raises:
            ServerSelectionTimeoutError: If the connection to MongoDB fails after all retries.
        """
        # Get the mongo_uri
        mongo_uri = settings.mongo_uri

        try:
            return MongoClient(mongo_uri, uuidRepresentation="standard", tz_aware=True)
        except ServerSelectionTimeoutError:
            time.sleep(3)
            logger.warning("MongoDB Server not found, attempting reconnection...")
            return self.connect_to_mongodb()

    def get_mongo_collection(self, col) -> Collection:
        """
        Fetches a specific MongoDB collection based on the database and collection names provided.

        Args:
            col (str): The name of the collection within the specified database.

        Returns:
            Collection: The desired collection object from the specified database.
        """

        return self.client[settings.db_name][col]
