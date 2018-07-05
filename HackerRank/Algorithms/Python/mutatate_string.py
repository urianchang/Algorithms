"""
Mutatations

https://www.hackerrank.com/challenges/python-mutations/problem
"""

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    return "".join(string_list)

print mutate_string('abracadabra', 5, 'k')
