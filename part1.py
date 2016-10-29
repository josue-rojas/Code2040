import requests
import re



r = requests.post("http://challenge.code2040.org/api/register", data={'token':'41d1df9d93182791bd6030e9db134736','github':'https://github.com/josuerojasrojas/Code2040'})
print r.text
