import httplib, urllib
import requests
import re
import json

"""print statements are just used to analyze and think about the problem"""

#get stuff
data={'token': '41d1df9d93182791bd6030e9db134736'}
r = requests.post("http://challenge.code2040.org/api/prefix", json=data)
#all text
text = r.text
print(text)
p = re.compile('\w+') #find all words
print

#all the words
words = p.findall(text)
prefix = words[1] #word to look for

#pattern to get words with the prefix
findAll = re.compile(prefix + '\w*') #pattern
print prefix
#all the words with the prefix
allPrefix = findAll.findall(text)
#remove all the undesires
print text


#remove all the words with the prefix
for non in allPrefix:
    words.remove(non)
words.remove("array")
words.remove("prefix")
print
print words

#encoding cause it was having trouble accepting 
print
wordT = (json.dumps(words)).encode('utf-8')
print wordT


#had to sepereate this cause it would not go through the api 
data={'token': '41d1df9d93182791bd6030e9db134736', 'array':words}

r = requests.post("http://challenge.code2040.org/api/prefix/validate", json=data)
print r.text
