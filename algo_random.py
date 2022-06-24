from typing import Sequence
from Classes.Action import Action
from utils import generate_random_portfolio, timer
from Classes.Portfolio import Portfolio
import random


@timer
def algo_random(items: Sequence[Action], loop: int, budget: int) -> Portfolio:
    """
    Returns the best portfolio from many
    random portofolios
    """
    best_portfolio = None
    count = 0
    for _ in range(loop):
        portfolio = generate_random_portfolio(budget, items)
        count += len(portfolio)
        best_portfolio = max(best_portfolio, portfolio)   
    print("------------------------------")
    print("{0:>10} {1:>10}   {2}".format("Cout", "Profit", "Portfolio"))            
    print(best_portfolio)
    print(count, "iterations")
    return best_portfolio, count
