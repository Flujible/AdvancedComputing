"""Defines the KVpair (Key/Value Pair) object that will be used for mapReduce processing"""

class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
