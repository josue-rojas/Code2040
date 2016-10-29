import httplib, urllib
import requests
import re
import json
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
r = requests.post("http://challenge.code2040.org/api/dating", data={'token': '41d1df9d93182791bd6030e9db134736'})
text = r.text
print text
digit = re.compile('\d+')
number = digit.findall(text)
interval = eval(number[-1])
print interval
bigNum = (eval(number[2]) * 86400) + (eval(number[3]) * 3600) + (eval(number[4]) * 60) + (eval(number[5]))
interval = interval + bigNum
days = (interval / 86400) 
interval = interval - (days*86400)
hour = (interval / 3600)
interval = interval - (hour*3600)
minutes = (interval / 60)
interval = interval - (minutes*60)
seconds = (interval % 60)

print days
print hour
print minutes
print seconds
print number

#replace
number[2] = days
number[3] = hour
number[4] = minutes
number[5] = seconds
#convert again
print number
dateS =  number[0] + "-"+ number[1]+ "-" + str(number[2])+ "T"+str(number[3]) + ":"+ str(number[4])+":"+str(number[5])+"Z"
print dateS





r = requests.post("http://challenge.code2040.org/api/dating/validate", data={'token': '41d1df9d93182791bd6030e9db134736', 'datestamp':dateS})
print r.text


