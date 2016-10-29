import requests
import re



r = requests.post("http://challenge.code2040.org/api/haystack", data={'token':'41d1df9d93182791bd6030e9db134736'})
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
