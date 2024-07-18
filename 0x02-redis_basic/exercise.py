#!/usr/bin/env python3
''' create cache class and do some operations on it'''
import redis
import uuid
from typing import Union


class Cache:
    '''cache class'''

    def __init__(self):
        '''init method'''
        self. _redis = redis.Redis()
        self. _redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store method'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
