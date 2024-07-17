#!/usr/bin/env python3
''' script provides stats about nginx logs stored in MongoDB'''
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()

    stat = client.logs.nginx
    total = stat.count_documents({})
    get = stat.count_documents({'method': 'GET'})
    post = stat.count_documents({'method': 'POST'})
    put = stat.count_documents({'method': 'PUT'})
    patch = stat.count_documents({'method': 'PATCH'})
    delete = stat.count_documents({'method': 'DELETE'})
    status = stat.count_documents({'method': 'GET', 'path': '/status'})

    print(f'{total} logs')
    print('Methods:')
    print(f'\tmethod GET: {get}')
    print(f'\tmethod POST: {post}')
    print(f'\tmethod PUT: {put}')
    print(f'\tmethod PATCH: {patch}')
    print(f'\tmethod DELETE: {delete}')
    print(f'{status} status check')

    client.close()
