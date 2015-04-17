class queue(object):
    
    def __init__(self):
        self.vals = []
    
    def insert(self,aval):
        self.vals.append(aval)
    
    def remove(self):
        
        if len(self.vals) > 0:
            self.vals = self.vals[1:]
        else:
            raise ValueError
        
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


a = queue()
a.insert(4)
a.insert(5)
print a
a.remove()
print a