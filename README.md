# Python

## files with python

file access modes
- `r`   : needs to exist or shows error
- `w`   : if exists, overwritten
- `a`   : if exists, append
- `b`   : open in binary mode
- `+`   : open for updating (reading / writing)
- `t`   : open as text
<br>

1. files are open as `rt` by default.
2. access modes can be combined like `r+` for reading and updating.
3. cannot combine `r`, `w`, `a` as well as `b`, `t`.
4. `t` is default therefore usually ommitted.
5. difference between `t` and `b` are `str` and `bytes`. in case of writing in byte mode, it should be `wb`.
6. after file was open, it must be closed.
<br>

example
```python
my_file = open(file.txt, 'w')
...
my_file.close()
```
<br>

