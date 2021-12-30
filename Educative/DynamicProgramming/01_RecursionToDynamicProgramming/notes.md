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

Recursion can be an excellent brute force technique, but the solutions may have high time complexity.

**Dynamic programming**: name of solving problems that depend on subproblems. Memorization 
techniques are an addition to dynamic programming.

Two basic approaches:
1. Bottom-up: start from the most basic unit (sub-problem) and then build up to the problem.
2. Top-down: start from the problem and build and use smaller components as needed
    * Recursion is essentially the top-down approach

Prerequisites to using dynamic programming:
* optimal substructure: optimal solution to a problem can be build using the optimal solutions
of the problem's subproblems
* overlapping subproblems: repeating subproblems avoid recomputation

The ability to express an algorithm recursively does not mean that algorithm has an optimal substructure.
