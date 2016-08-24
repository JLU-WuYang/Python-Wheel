# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import MySQLdb
import traceback
import copy
class UnitManager(object):
    def __init__(self,username,password,database):
        self.db = MySQLdb.connect("localhost", username, password, database, charset='utf8')
                
        self.cursor = self.db.cursor()
        print "connect"
    
    def __del__(self):
        self.db.close()
        print "throw"
    
    def execute(self,sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            
        except :
            # 发生错误时回滚
            traceback.print_exc() 
            self.db.rollback() 
    
    def store(self,Object):
        dic={"<type 'str'>":"varchar(10)","<type 'int'>":"int"}
        stri=""
        for name,typ in vars(Object).items():
            print name,type(typ),dic[str(type(typ))]
            stri=stri+name+" "+dic[str(type(typ))]+","
        stri=stri[:-1]      
        sql="create table "+Object.__class__.__name__+"("+stri+");"
        self.execute(sql)
        print "Success Create Table"
    
    def drop(self,Object):
        sql="drop table "+Object.__class__.__name__
        self.execute(sql)
        print "Success Drop Table"
    
    def insert(self,Object):
        stri=""
        for name,typ in vars(Object).items():
            stri=stri+"'"+str(typ)+"'"+","      
        stri=stri[:-1]
        sql="insert into "+Object.__class__.__name__+" values("+stri+");"
        
        self.execute(sql)
        print "Success Insert"
    
    def select(self,Object):
        sql="select * from " +Object.__class__.__name__
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        lis=vars(Object).items()
        
        Object_lis=[]
        for line in results:
            dic={}
            for i in xrange(len(lis)):
                dic[lis[i][0]]=line[i]
            Copy=copy.deepcopy(Object)   
            Object_lis.append(Copy.setter(dic))
        print "Success select"
        return Object_lis
            
            
        

class student(object):
    def __init__(self):
        self.a=''
        self.b=0
    def setter(self,dic):
        self.a=dic['a']
        self.b=dic['b']
        return self
if __name__=="__main__":
    um=UnitManager()
    
    #um.store(student())
    #um.drop(student())
    s=student()
    s.a='qq'
    s.b=2
    um.insert(s) 
    s.b=1
    um.insert(s)
    #print dir(s)
    lis=um.select(student())
    for line in lis:
        print line.a,line.b
    
    
    
   
    
    
    
    
        
