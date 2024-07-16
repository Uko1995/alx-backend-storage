#!/usr/bin/env python3
'''module has a function that changes all topics of s school document based on
   name'''


def update_topics(mongo_collection, name, topics):
    ''' function that changes topics'''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
