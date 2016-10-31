import requests
import re
import json



r = requests.post("http://challenge.code2040.org/api/haystack", data={'token':'41d1df9d93182791bd6030e9db134736'})
""""
#shorter way
#this was done after everything was submitted and I found out about json
#this is not meant to be understood i just wanted to squish everything together
index =  json.loads(r.text)['haystack'].index(json.loads(r.text)['needle']) #(extra short if you put this straight in the post, but will be too long and confusing
                             
r = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token':'41d1df9d93182791bd6030e9db134736','needle':index})

print r.text
#if doing it this way ignore everything else
"""
text =  r.text #not neccesary but just wanted to see the word
print text
p = re.compile('\w+') #find all words (just the pattern)
words = p.findall(text)
needle = words[1]
print needle

#remove unnnecessary words
words.remove('needle')
words.remove('haystack')
words.remove(needle) #remove the first instance, leaving the other behind

#finanlly the index
index = words.index(needle)
print index

#post it
r = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token':'41d1df9d93182791bd6030e9db134736','needle':index})
print r.text

