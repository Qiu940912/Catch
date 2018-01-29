#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
import xml.sax
import re
import MySQLdb 

count=0
#global count
list=[]
class DblpHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.author = ""
      self.title = ""
      self.year = ""
       
   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "article":
         print "****Article*****"
         global count
         count=count+1
         print count
      elif tag=="inproceedings":
         exit()
         
        # title = attributes["title"]
        #print "Title:", title
 
   # 元素结束事件处理
   def endElement(self, tag):
      #list=[]
      
      if self.CurrentData == "author":
         #count=cpunt+1
         print "Author:", self.author
         list.append(self.author)
        # print list
      elif self.CurrentData == "title":
         print "Title:", self.title
         list.append(self.title)
        # print list
      elif self.CurrentData == "year":
         print "Year:", self.year
         list.append(self.year)
         print list
         len1=len(list)
         year=list[len1-1]
         title=list[len1-2]
         list.pop(len1-1)
         list.pop(len1-2)
         author=','.join(list)
         print author
         sqli="insert into dblp values(null,%s,%s,%s)" 
         cur.execute(sqli,(author,title,year))
         conn.commit()
        # sql1.post(author,title,year)
         print list,title,year
        # print list
          
        # if len(list)==3:
         list[:]=[]
      self.CurrentData = ""
 
   # 内容事件处理
   def characters(self, content):
      if self.CurrentData == "author":
         self.author = content
      elif self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "year":
         self.year = content
         self.description = content
   #def append(data):
   #   list.append(data)
   #   print "list len:",len(list)
   #   if len(list)==4:
   #      print list
   #      list=[]
  
if ( __name__ == "__main__"):
   conn= MySQLdb.connect(                                                    
       host='localhost',                                                      
       port = 3306,                                                           
       user='root',                                                          
       passwd='123456',                                                     
       db ='DBLP',                                                            
       )                                                                     
   cur = conn.cursor()
   print "123124233456456768"
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
 
   # 重写 ContextHandler
   Handler = DblpHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("dblp.xml")
 
