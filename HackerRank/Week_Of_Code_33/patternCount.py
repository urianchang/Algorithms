"""
Pattern Count:

A string 's' contains many patterns of the form 1(0+)1
where (0+) represents any non-empty consecutive sequence
of 0's. The patterns are allowed to overlap.

You have to answer 'q' queries, each containing a string 's'.
For each query, find and print the total number of patterns
of the form 1(0+)1 that occur in 's'.
"""

def patternCount(s):
    # Complete this function
    counter = 0
    started = False
    for i in range(0, len(s)):
        if started == False and s[i] == "1":
            started = True
        elif started == True and s[i] == "1":
            if s[i-1] == "0":
                counter += 1
            else:
                continue
        elif started == True and s[i] == "0":
            continue
        else:
            started = False
    return counter

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)

"""
Input:
3
100001abc101
1001ab010abc01001
1001010001

Output:
2
2
3
"""
