**# Addition Calculator

status : 

last update: 15- jun- 2023

author : Daedra**
<hr/>

Visit [Project Gutemberg](https://www.gutenberg.org/) and find a few texts you'd like to analyze. 
Download the text files for these works, or copy the raw text from your browser into
a text file on your computer.

You can use the _count()_ method to find out how many times a word or phrase appears in a string. 
For example, the following code counts the number of times 'row' appears in a string.

```python 
line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')
```

Notice that converting the string to lowercase using _lower()_ catches all appearances of the word your're
looking for, regardless of how it's formatted. 

Write a program that reads the files you found at Project Gutenberg and determines how many times
the word _'the'_ appears in each text. This will be
an approximation because it will also count words such as _'then'_ and _'there'_.

Try counting  _'the '_, with a space in the string, and see how much lower your count is. 
