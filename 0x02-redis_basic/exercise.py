#!/usr/bin/env python3
"""
Exercise
"""
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

    def store(self, value):
        key = str(uuid4())
        self._redis.set(key, value)
        return key

    def get(self, key, fn=None):
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
