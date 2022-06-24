import csv
from time import time
import random
from itertools import combinations
from Classes.Action import Action
from Classes.Portfolio import Portfolio

def item_list(csv_file):
    """
    Return a list of actions object contained in a CSV
    """
    with open(csv_file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        return [Action(name=row['name'],
                       price=float(row['price']),
                       relative_profit=float(row['profit']))
                for row in reader
                if float(row['price']) > 0
                and float(row['profit']) > 0]


def find_next_combination(items, min_rep, max_rep):
    """
    Generate all the possible combination of a portfolio
    """
    for rep in range(min_rep, max_rep):
        for cmb in combinations(items, rep):
            yield cmb


def timer(func):
    """
    This function shows the execution time of
    the function object passed    
    """
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


def get_max_amount_of_items(list_actions, budget, reverse=True):
    """
    Return the number of actions we can save based on
    the budget
    """
    price = 0
    list_actions.sort(key=lambda x: x.price, reverse=reverse)
    for i, action in enumerate(list_actions):
        if price + action.price <= budget:
            price += action.price
        else:
            return i


def generate_random_portfolio(budget, items):
    """
    """
    portfolio = Portfolio(max_price=budget)
    data = items.copy()
    while data:
        random_action = data.pop(random.randint(0, len(data)-1))
        if not portfolio.add(random_action): 
            return portfolio
