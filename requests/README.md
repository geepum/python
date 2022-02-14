#### GET request

example
```python
import requests
r = requests.get('https://google.com')
print(r) # <Response [200]>
print(r.status_code) # 200
print(r.text)
print(r.encoding)
print(r.headers['Content-type']) # headers are not case sensitive
```
<br>

#### query parameters

example
```python
def google_search(query, num):
  r = requests.get('https://google.com/search', params={'q': query, 'n': num})
  
  return r.url

print(google_search('python', 10))
# https://www.google.com/search?q=python&num=1
```
<br>