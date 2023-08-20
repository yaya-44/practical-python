# report.py
#
# Exercise 2.4

import csv 
def read_portfolio(filename):
    ''' read portfolio from filename and return list of dictionaries '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append({'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])})
    return portfolio

def read_prices(filename):
    ''' read proces from filename and return dictionary '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
            else:
                print("Bad row", row)
    return prices

def compute_gain_or_loss(filename_portfolio, filename_prices):
    portfolio = read_portfolio(filename_portfolio)
    prices = read_prices(filename_prices)
    Gain = {}
    TotalGain = 0
    for s in portfolio:
        if s['name'] in prices:
            Gain[s['name']] = s['shares'] * (s['price'] - prices[s['name']])
            TotalGain += s['shares'] * (s['price'] - prices[s['name']])
    
    return  TotalGain, Gain

def make_report(filename_portfolio, filename_prices):
    portfolio = read_portfolio(filename_portfolio)
    prices = read_prices(filename_prices)
    report = []
    for s in portfolio:
        if s['name'] in prices:
            report.append((s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price']))
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10s %10.2f' % (r[0], r[1], f'${r[2]:.2f}', r[3]))
    return report
      






