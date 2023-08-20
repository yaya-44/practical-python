# pcost.py
#
# Exercise 1.27

import sys
def portfolio_cost(filename):
    total_cost = 0
    file = open(filename, 'rt')
    headers = next(file).split(',')
    for line in file:
        try:
            line = line.split(',')
            total_cost = total_cost + int(line[1]) * float(line[2])
        except ValueError:
            print("Couldn't parse", line)
    file.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)