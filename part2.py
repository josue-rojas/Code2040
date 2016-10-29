import requests
import re



r = requests.post("http://challenge.code2040.org/api/reverse", data={'token':'41d1df9d93182791bd6030e9db134736'})
print r.text #not neccesary but just wanted to see the word

#reverse is in the end 
r = requests.post("http://challenge.code2040.org/api/reverse/validate", data={'token':'41d1df9d93182791bd6030e9db134736','string':r.text[::-1]})
print r.text
