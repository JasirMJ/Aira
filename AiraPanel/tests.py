from django.test import TestCase

# Create your tests here.
import json

# some JSON:
x = '[{ "name":"John", "age":30, "city":"New York"},{ "name":"John", "age":30, "city":"New York"}]'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(len(y))
for x in y:
    print(x['name'])
