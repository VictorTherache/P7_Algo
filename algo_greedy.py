import random
from Classes.Portfolio import Portfolio
from utils import timer
from multiprocessing.pool import ThreadPool as Pool


@timer
def algo_greedy(items, budget):
    """
    Return a portfolio based on the actions ratio
    price/profit
    """
    portfolio = Portfolio(max_price=budget)
    sorted_items = sorted(items,
                          key=lambda x: x.price / x.relative_profit
                          )
    for item in sorted_items:
        if not portfolio.add(item):
            break
    print("------------------------------")
    print("{0:>10} {1:>10}   {2}".format("Cout", "Profit", "Portfolio"))        
    print(portfolio)
    return portfolio
