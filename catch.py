#coding:utf-8
import urllib2
import urllib
import xml.sax
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#soup = BeautifulSoup(open('test.html'))
soup=BeautifulSoup(html)
#print soup.prettify()
soupa=[soup.title,soup.head,soup.p,soup.a]
for x in soupa:
    print x









#values = {}
#values['username'] = "2268206064@qq.com"
#values['password'] = "Love940912,"
#data = urllib.urlencode(values) 
#url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#request = urllib2.Request(url,data)
#try:
 #   response = urllib2.urlopen(request)
  #  print response.read()
#except urllib2.HTTPError, e:
 #   print e.code
#except urllib2.URLError, e:
 #   print e.reason
