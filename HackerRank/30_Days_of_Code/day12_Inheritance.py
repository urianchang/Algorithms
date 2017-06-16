"""
Day 12: Inheritance

You are given two classes, Person and Student, where Person
is the base class and Student is the derived class. Completed
code for Person and a declaration for Student are provided for
you in the editor. Observe that Student inherits all the properties
of Person.

Complete Student class by writing the following:
    * A Student class constructor, which has 4 parameters:
        1. A string, firstName
        2. A string, lastName
        3. An integer, id
        4. An integer array of test scores, scores
    * A char calculate() method that calculates a Student object's
    average and returns the grade character representative of their
    calculated average.
"""

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = 0
        for i in range(len(self.scores)):
            total += self.scores[i]
        average = total / len(self.scores)
        if average >= 90 and average <= 100:
            return "O"
        elif average >= 80 and average < 90:
            return "E"
        elif average >= 70 and average < 80:
            return "A"
        elif average >= 55 and average < 70:
            return "P"
        elif average >= 40 and average < 55:
            return "D"
        else:
            return "T"
