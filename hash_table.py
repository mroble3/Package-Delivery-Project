class HashMap:
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

        # Make hash key has a Space-time capacity of 0(1)
    def make_hash_key(self, key):
        return int(key) % len(self.map)

        # Insert new package value into hash table
        # Space-time complexity is 0(N)
    def insert(self, key, value):
        key_hash = self.make_hash_key(key)
        key_value = [key, value]

        if self.map[key_hash] == None:
                    self.map[key_hash] = list([key_value])
                    return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

        # Update the package
        # Space-time complexity is 0(n)
    def update(self, key, value):
        key_hash = self.make_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True

        else:
            print('There was an error with updating on key: ' + key)

    # Retrieve a value from the hash table
    # Space-time complexity is 0(n)
    def get_value(self, key):
        key_hash = self.make_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

        # Remove a value from hash table Runtime is 0(n)
        def delete(self,key):
            key_hash = self.make_hash_key(key)

            if self.map[key_hash] is None:
                return False
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                    return True
            return False




