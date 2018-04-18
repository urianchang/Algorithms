"""
Average Rating of Top Employees

URL: https://www.hackerrank.com/contests/w37/challenges/the-average-rating-of-top-employees
"""
import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    bonus_round = [emp for emp in rating if emp >= 90]
    avg_rating = (float(sum(bonus_round))/len(bonus_round)) + 0.001
    print("%.2f" % avg_rating)

if __name__ == '__main__':
    n = int(raw_input())

    rating = []

    for _ in xrange(n):
        rating_item = int(raw_input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
