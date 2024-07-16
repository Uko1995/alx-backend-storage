#!/usr/bin/env python3
'''function that lists alldocuments in a collection'''


def list_all(mongo_collection):
    '''lists all documents in collection'''
    documents = list(mongo_collection.find())
    return documents
