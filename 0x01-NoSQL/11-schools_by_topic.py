#!/usr/bin/env python3
''' module with a function that returns the list of school having a topic'''


def schools_by_topic(mongo_collection, topic):
    '''function that returns the list of schools'''
    sch = list(mongo_collection.find({'topic': topic}))
    return sch
