# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import csv 

def read_portfolio(filename):
    ''' read portfolio from filename and return list of dictionaries '''
    return parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    ''' read prices from filename and return dictionary '''
    return dict(parse_csv(filename, types=[str, float], has_headers=False))

def make_report_data(portfolio,prices):
    report = []
    for stock in portfolio:
        if stock['name'] in prices:
            report.append((stock['name'], stock['shares'], prices[stock['name']], prices[stock['name']] - stock['price']))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10s %10.2f' % (r[0], r[1], f'${r[2]:.2f}', r[3]))

def portfolio_report(filename_portfolio, filename_prices):
    portfolio = read_portfolio(filename_portfolio)
    prices = read_prices(filename_prices)
    report = make_report_data(portfolio, prices)
    print_report(report)
    return report
      

    
portfolio_report('Work/Data/portfoliodate.csv', 'Work/Data/prices.csv')



