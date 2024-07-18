#!/usr/bin/env python3
''' create cache class and do some operations on it'''
import redis
import uuid
from typing import Union, Any, Callable


class Cache:
    '''cache class'''

    def __init__(self) -> None:
        '''__init__ method'''
        self. _redis = redis.Redis()
        self. _redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store method'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        '''get method'''
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(data)

    def get_int(self, key: str) -> int:
        '''get_int method'''
        return int(self._redis.get(key)) if self._redis.get(key) else 0

    def get_int(self, key: str) -> str:
        '''get_str method'''
        data = self._redis.get(key)
        return data.decode('UTF-8') if data else ''
