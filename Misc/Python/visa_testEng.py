"""
Amazing Strings
"""

def thing(l):
    # Create list to hold solutions
    s = []
    # Iterate through list of words
    for w in l:
        n = 0   # number of substitutions
        i = 1 # index to evaluate upon
        # Iterate through each character in the word
        while i < len(w):
            # If current character is equal to character before it...
            if w[i] == w[i - 1]:
                # Increase number of substitutions by 1
                n += 1
                # Increase index by 2 to evaluate next pair
                i += 2
            else:
                # Increase index by 1 to evaluate next character
                i += 1
        # Append number of substitutions to list of solutions
        s.append(n)
    # Return list of solutions
    return s

ls = ['ab', 'aab', 'abb', 'abab', 'abaaaba']
print thing(ls)     # [0, 1, 1, 0, 1]


"""
Replace Me
"""

def r(s):
    ns = "" # New string to be returned
    a = s.split(' ') # Split string into list of words
    # Iterate through list of words
    for w in a:
        # If word is "is"
        if w == "is":
            # Add "is not" to the new string
            ns += "is not "
        else:
            # Add word to new string
            ns += w + " "
    return ns

strRep = raw_input()
print r(strRep)
