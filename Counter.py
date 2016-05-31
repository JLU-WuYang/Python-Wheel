class Counter:
    """
    c=Counter()
    s=[9,8,7]
    for i in s:
        c.insert(i)
    for line in  c.getDic():
        print line

    """    
    
    def __init__(self):
        self.dic={}
    def insert(self,Object):
        if self.dic.has_key(Object):
            self.dic[Object]=self.dic[Object]+1
        else:
            self.dic[Object]=1
    def count(self,Object):
        if self.dic.has_key(Object):
            return self.dic[Object]
        else:
            return 0
    def getDic(self):
        return self.dic
