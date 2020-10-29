import requests
import json
import sys
x = sys.argv[1]
op = sys.argv[2]
y = sys.argv[3]
try:

	IP = sys.argv[4]
	PORT = sys.argv[5]

except IndexError:

	IP = 'localhost'
	PORT = 5000

print(op)

payload = { 'x' : str(x) , 'y' : str(y)}
myheaders = {'content-type' : 'application/json'}

if op == '+':

	url = 'http://%s:%s/v1/ressources/calculator/add' % (IP , PORT)

if op == '-':

	url = 'http://%s:%s/v1/ressources/calculator/sub' % (IP , PORT)

if op == '*':

	url = 'http://%s:%s/v1/ressources/calculator/mult' % (IP , PORT)


if op == '/':

	url = 'http://%s:%s/v1/ressources/calculator/div' % (IP , PORT)





resp = requests.post(url , data = json.dumps(payload) , headers = myheaders)

print(resp.json())