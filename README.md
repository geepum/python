# Python

- [read and write files](https://github.com/geepum/python/tree/main/files)
- [requests](https://github.com/geepum/python/tree/main/requests)
- [json](https://github.com/geepum/python)

## Learnings

### Errors

- NameError
  - If not defined or wrongly defined.
```python
print(a + b)
a = 0
b = 5
# NameError: name 'a' is not defined
```

- TypeError
  - If an operation applied to inappropriate types.
```python
print("15" + 2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- ValueError
  - Correct type but with inappropriate value.
```python
print(int("five"))
# ValueError: invalid literal for int() with base 10: 'five'
```

- ZeroDivisionError
```python
a = 0
b = 5
print(b / a)
# ZeroDivisionError: division by zero
```

- SyntaxError
```python
# 1
new_list = [1, 2, 3, 4, 5
print(new_list)

# 2
i := 3

# SyntaxError: invalid syntax
```

- OSError
```python
f = open('i_dont_exist.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'i_dont_exist.txt'
```

- ImportError
```python
from math import square
# ImportError: cannot import name 'square'
```

- EOFerror
  - One case can be when input has no data to read.
```python
first = input()
second = input()
third = input()   # this was not expected

# EOFError: EOF when reading a line
```

- IndexError
```python
new_list = ['the only element']
print(new_list[1])
# IndexError: list index out of range
```


