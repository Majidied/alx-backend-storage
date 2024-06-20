#!/usr/bin/env python3
"""
Exercise
"""
from typing import Union
from redis.client import Redis
from uuid import uuid4


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in redis with randomly generated key
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get(self, key, fn=None):
        """
        Get data from redis
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Convert bytes to str
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Convert bytes to int
        """
        return self.get(key, lambda x: int(x))
