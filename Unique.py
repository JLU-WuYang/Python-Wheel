class Unique:
    """
    u=Unique()
    s=['a','b','a',1,1.0]
    for i in s:
        if  not u.exist(i):
            u.insert(i)
    d=u.getDic()
    for line in d:
        print line
    """
    def __init__(self):
        self.dic={}
    def insert(self,Object):
        self.dic[Object]=1
    def exist(self,Object):
        return self.dic.has_key(Object)
    def length(self):
        return len(self.dic)
    def getDic(self):
        return self.dic
