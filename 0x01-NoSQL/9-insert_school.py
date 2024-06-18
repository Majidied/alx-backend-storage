#!/usr/bin/env python3
"""
Insert a document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        kwargs (dict): The document to insert.

    Returns:
        str: The new _id for the new document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
