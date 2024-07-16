#!/usr/bin/env python3
'''function that inserts a new document in a collection'''


def insert_school(mongo_collection, **kwargs):
    '''adds a new document in collection'''
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
