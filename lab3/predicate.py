class Family:
    def __init__(self):
        self.parent = {
            'John': ['Mary', 'Mike'],
            'Sarah': ['Mary'],
            'David': ['Mike']
        }

    def is_parent(self, x, y):
        """Returns True if x is a parent of y."""
        return y in self.parent.get(x, [])

    def is_sibling(self, x, y):
        """Returns True if x and y are siblings."""
        for parent, children in self.parent.items():
            if x in children and y in children and x != y:
                return True
        return False

family = Family()


print(family.is_parent('John', 'Mary'))
print(family.is_parent('Sarah', 'Mike')) 
print(family.is_sibling('Mary', 'Mike'))
