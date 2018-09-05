from Crypto.Hash import SHA256 as hashFunction

class Block:
    def __init__(self, transaction=None, value=0, parent_hash=None, height=0, timestamp=0):
        self.height = height
        self.transaction = transaction
        self.value = value
        self.parent_hash = parent_hash
        self.timestamp = timestamp
        self.hash = self.hash_self()

    def __str__(self):
        return "block height:%s; transactions contained: %s; value: %s; parent hash: %s; current block hash: %s.\n" % (self.height, self.transaction, self.value, self.parent_hash, self.hash)

    def hash_self(self):
        hash = hashFunction.new()
        hash.update((str(self.height) + 
                    str(self.value) +
                    str(self.transaction) + 
                    str(self.parent_hash)).encode() +
                    str(self.timestamp).encode())
        return hash.hexdigest()
    
    __repr__ = __str__