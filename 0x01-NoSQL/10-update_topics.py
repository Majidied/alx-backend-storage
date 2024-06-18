#!/usr/bin/env python3
"""
Update a MongoDB document.
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update a MongoDB document.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
        name (str): The name of the document to update.
        topics (list): The list of topics to set for the document.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
