class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        hash_idx = int(self.horner_hash(key))
        #print('hash_idx: ', hash_idx)
        # quadratically probe when you get a collision
        #print('where to shit: ', self.hash_table[hash_idx])
        if self.hash_table[hash_idx] is not None and self.hash_table[hash_idx][0] != key:
            new_idx = self.quadratic_probing(hash_idx) # give the key's idx into the quadratic probe
            self.hash_table[new_idx] = [key, value] # you have to feed the value that caused collision into the system somehow
            #print('new idx: ', new_idx, [key, value])
            #print('it shit here')
        elif self.hash_table[hash_idx] is None:
            self.hash_table[hash_idx] = [key, value]
            #print('it super shitted here')
        elif self.hash_table[hash_idx][0] == key:
            #print('is government being reinserted? ', value)
            self.hash_table[hash_idx][1] = value # replace the current value

        self.num_items += 1 # increment number of items

        # resize and rehash if the load factor is too much
        if (self.num_items / self.table_size) > 0.5:
            self.resize()
            self.rehash()


    def rehash(self):
        res = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                res.append(self.hash_table[i]) # [ idx, tuple ]

        self.hash_table = self.table_size * [None]
        self.num_items = 0  # reset the number of items

        for i in res:
            hash_idx = int(self.horner_hash(i[0]))
            #print('hash idx at rehash: ', hash_idx)
            # quadratically probe when you get a collision
            if self.hash_table[hash_idx] is not None and self.hash_table[hash_idx][0] != i[0]:
                new_idx = self.quadratic_probing(hash_idx)  # give the key's idx into the quadratic probe
                self.hash_table[new_idx] = i  # you have to feed the value that caused collision into the system somehow
            elif self.hash_table[hash_idx] is None:
                self.hash_table[hash_idx] = i
            elif self.hash_table[hash_idx][0] == i[0]:
                self.hash_table[hash_idx][1] = i[1]  # replace the current value

            self.num_items += 1  # increment number of items


    def resize(self):
        self.table_size = (self.table_size * 2) + 1
        self.hash_table += [None] * (self.table_size - len(self.hash_table)) # extend the table by as many cells it's been increased by

    def quadratic_probing(self, hash_idx):
        probe = 0
        tmp = hash_idx
        while self.hash_table[tmp] is not None:
            tmp = (hash_idx + (probe ** 2)) % self.table_size
            probe += 1

        return tmp


    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        n = min(len(key), 8)
        hash_idx = 0
        #print('horner hash key: ', key)
        #print('len of hash key: ', len(key))
        for i in range(len(key)):
            hash_idx += ord(key[i]) * (31 ** (n - 1 - i))
            #print('horner hash idx: ', hash_idx)
        return hash_idx % self.table_size

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        for i in self.hash_table:
            if i is None:
                continue
            else:
                if i[0] == key:
                    return True
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        for i in range(self.table_size):
            if self.hash_table[i] is None:
                continue
            elif self.hash_table[i][0] == key:
                return i
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        res = []
        for i in self.hash_table:
            if i is None:
                continue
            else:
                res.append(i[0])
        return res

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        for i in self.hash_table:
            if i is not None:
                if i[0] == key:
                    return i[1]
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size

