#!/usr/bin/env pythons3
'''function returns all students sorted by average score'''


def top_students(mongo_collection):
    ''' function returns sy=tudents by average score'''
    top = mongo_collection.aggregate([
        {'$project': {
            'name': 1,
            'averageScore': {'$avg': '$topics.score'}
            }},
        {'$sort': {'averageScore': -1}}])

    return top
