import requests
import sys
import json
import time

url = 'http://server:8080/db/'

r = requests.post(url + 'john', json={'first_name': 'john', 'last_name': 'smith'})
if r.status_code != 200:
    print('failed to set')
    sys.exit(1)

r = requests.get(url + 'john')
if r.status_code != 200:
    print('failed to get')
    sys.exit(2)

person = r.json()
print('found person:')
print(json.dumps(person))
print('')
print('All tests past! to make bobs build fail exit a none-zero e.g. sys.exit(1)')
