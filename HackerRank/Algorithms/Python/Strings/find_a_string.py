"""
Find a string

https://www.hackerrank.com/challenges/find-a-string/problem
"""

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

print count_substring('asdfas', 'as')
