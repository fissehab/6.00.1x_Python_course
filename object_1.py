class fish(object):
    """
    I am doing this for fun and to enhance my python skill"""
    
    def __init__(self):
        self.vals=[]
        self.answer =[]
        self.length= 0
    def insert(self,e):
        if not e in self.vals:
         self.vals.append(e)
         
         
    def member(self,e):
        return e in self.vals
        
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self,e):
        
        for i in e:
            if i in self.vals:
                self.answer.append(i)
        return self.answer
        
    def len(self):
      for i in self.vals:
        self.length+=1
      return self.length