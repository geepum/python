#### file access modes

- `r`   : needs to exist or shows error
- `w`   : if exists, overwritten.
- `a`   : if exists, append.
- `b`   : open in binary mode
- `+`   : open for updating (reading / writing). cannot be used alone. cannot truncate (reduce).
- `t`   : open as text
<br>

1. files are open as `rt` by default.
2. access modes can be combined like `r+` for reading and updating.
3. cannot combine `r`, `w`, `a` as well as `b`, `t`.
4. `t` is default therefore usually ommitted.
5. difference between `t` and `b` are `str` and `bytes`. in case of writing in byte mode, it should be `wb`.
6. after file was open, it must be closed.
7. encoding is for text files only. binaries do not need encoding.
<br>

example
```python
my_file = open(file.txt, 'w')
...
my_file.close()
```
[other examples](https://www.codegrepper.com/code-examples/python/file+access+modes+in+python)
<br>

#### read files

byte size
- `\n` is also 1 byte character
<br>

read(size)
- size: bytes of the file
<br>

readline(size)
- size: bytes of a single line
- adds `\n` at the end by default
<br>

readlines()
- the whole file becomes a list
- each line becomes an array of the list
- all byte characters are read as an array. newline becomes part of a line as `\n` at the end of a line.
<br>

for loop
- most efficient way
- adds `\n` after each iteration
```python
file = open('animals.txt', 'r')
for line in file:
  print(line)
```
<br>

#### write or append to files

example1
```python
names = ['geepum', 'terry', 'june', 'kevin']

file = open('names.txt', 'w', encoding='utf-8')

for name in names:
  file.write(name + '\n')

file.close()
```
<br>

example2
```python
names = ['geepum\n', 'terry\n', 'june\n', 'kevin\n']

file = open('names.txt', 'w', encoding='utf-8')
file.writelines(names)
file.close()
```
<br>

example3
```python
file = open('names.txt', 'a', encoding='utf-8')
file.write('julie\n')
file.close()
```
<br>

#### context manager

example
```python
# test.txt has a word - file
with open('test.txt', 'r') as f:
  name = f.read()
  # create file1 - file10
  for i in range(1, 11):
    with open(f'{name}{i}.txt', 'w', encoding='utf-8') as file:
      # write 1 to file1...10 to file10
      file.write(f'{i}')
```