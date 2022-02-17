#### conversion table for encoding from python to json

| python | json |
| :---: | :---: |
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

> custom classes such as datetime objects cannot be converted to json that easy.
<br>

#### serialization

example - json.dump()
```python
# python objects to json - file-like
import json

with open('json_file.json', 'w') as json_file:
  json.dump(python_dictionary, json_file)
```
<br>

example - json.dumps()
```python
# python objects to json - string-like
import json

json_str = json.dumps(python_dictionary, indent=2) # saves the string in a prettified format
print(json-str) # prints json as string
```
<br>

#### deserialization

example - json.load()
```python
# json to python object - file-like
json.load()

# json to python object - string-like
json.loads()
```
<br>
