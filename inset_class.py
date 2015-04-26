class intset(object):
     def __init__(self):
        self.vals=[]
     def insert(self,e):
         if not e in self.vals:
             self.vals.append(e)
     def member(self,e):
         return e in self.vals
     def remove(self,e):
         try:
             self.vals.remove(e)
         except:
             raise ValueError(str(e) +'  not found')
             
     def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
