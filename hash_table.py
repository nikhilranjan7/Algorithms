"""Hash Function is
    (ASCII value of First letter * 100) + ASCII value of Second letter"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        val = hash_table.calculate_hash_value(string)
        if self.table[val] == None:
            self.table[val]=[string]
        else:
            self.table[val].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        if self.table[hash_table.calculate_hash_value(string)] == None:
            return -1
        return hash_table.calculate_hash_value(string)

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hv = ord(string[0])*100 + ord(string[1])
        return hv

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
