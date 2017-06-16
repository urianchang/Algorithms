"""
Day 13: Abstract Classes

Given a Book class and a Solution class, write a MyBook class
that does the following:
    * Inherits from Book
    * Has a parameterized constructor taking these 3 parameters:
        1. string title
        2. string author
        3. int price
    * Implements the Book class' abstract display() method so it prints these 3 lines:
        1. Title:, a space, and then the current instance's title
        2. Author:, a space, and then the current instance's author
        3. Price:, a space, and then the current instance's price
"""
from abc import ABCMeta, abstractmethod

class Book:
    __metaclass__ = ABCMeta
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(): pass
    
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print "Title:", self.title
        print "Author:", self.author
        print "Price:", self.price
