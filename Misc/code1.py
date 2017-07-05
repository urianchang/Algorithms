"""
Find the sentence containing the largest number
of words in some given text. The text is specified
as a string S consisting of N characters: letters,
spaces, dots (.), question marks (?) and exclamation
marks (!).
"""

def solution(S):
    sentences = []
    string = ""
    # Iterate through the string to make list of sentences
    for char in S:
        if char == "." or char == "!" or char == "?":
            sentences.append(string)
            string = ""
        else:
            string = string + char
    maxWords = 0
    # Iterate through each sentence to find max word count
    for sentence in sentences:
        words = sentence.split()
        if len(words) > maxWords:
            maxWords = len(words)
    return maxWords

S1 = "We test coders. Give us a try?"
print "Largest number of words:", solution(S1)
S2 = "Forget CVs..Save time . x x"
print "Largest number of words:", solution(S2)
