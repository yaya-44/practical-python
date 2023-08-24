# pcost.py
#
# Exercise 1.27
import csv
import sys
from fileparse import parse_csv

def portfolio_cost(filename):
    portfolio = parse_csv(filename, select=['shares', 'price'], types=[int, float])
    total_cost = 0
    for row in portfolio:
        total_cost += row['shares'] * row['price']
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)