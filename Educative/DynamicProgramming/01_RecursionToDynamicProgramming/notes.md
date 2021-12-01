# NOTES
**Direct recursion**: function calls itself directly in body or function.
**Indirect recursion**: Two or more functions call themselves indirectly from each other.
**Linear recursion**: Single call to functions
**Non-linear recursion**: Call function multiple times

Example:

```python 
# input
str = "abacada"
char = 'a'

# output
countChar("abacada", 'a') = 4

# complete helper function
def countChar(str, char):
    '''
    you can call helper function as countChar_(str[1:], char)
    '''
    if len(str) == 0:
        return 0
    if str[0] == char:
        return 1 + countChar_(str[1:], char)
    return countChar_(str[1:], char)

```

