class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, other):
        append_return = intSet()
        assert type(self) == type(other)
        for i in range(0,len(other.vals)):
            if other.vals[i] in self.vals:
                append_return.insert(other.vals[i])
                #append_return.append(other.vals[i])
        #return append_return
        return '{' + ','.join([str(e) for e in append_return.vals]) + '}'
        
s = intSet()
s.insert(3)
s.insert(4)
s.insert(5)

a = intSet()
a.insert(5)
a.insert(7)
a.insert(8)

print a.intersect(s)