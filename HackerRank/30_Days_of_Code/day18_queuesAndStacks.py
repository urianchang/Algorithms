"""
Day 18: Queues and Stacks

To solve this challenge, we must first take each character in 's',
enqueue it in a queue, and also push that same character onto a stack.
Once that's done, we must dequeue the first character from the queue
and pop the top character off the stack, then compare the two
characters to see if they are the same; as long as the characters match,
we continue dequeueing, popping, and comparing each character until our
containers are empty (a non-match means  isn't a palindrome).

Write the following declarations and implementations:
    1. Two instance variables: one for your stack, and one for your queue.
    2. A void pushCharacter(char ch) method that pushes a character onto a stack.
    3. A void enqueueCharacter(char ch) method that enqueues a character in the
       queue instance variable.
    4. A char popCharacter() method that pops and returns the character at the
       top of the stack instance variable.
    5. A char dequeueCharacter() method that dequeues and returns the first character
       in the queue instance variable.
"""

class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []
    def pushCharacter(self, ch):
        self.stack.append(ch)
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)
