````# Simpler code

status :

last update: 01- jun- 2023

author : Daedra
<hr/>

The program _file_reader.py_ in this section uses a temporary variable, lines,
to show how splitlines() works. You can skip the teporary vaialbe and loop
directly over the list that splitlines() returns.

```python
for line in lines.splitlines():
```

Remove the temporary variable from each of the programs in this section, to make them more concise.
````