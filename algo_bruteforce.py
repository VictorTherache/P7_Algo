from utils import (find_next_combination,
                   item_list,
                   timer,
                   get_max_amount_of_items
                   )
from Classes.Portfolio import Portfolio


@timer
def algo_brute_force(items, budget):
    """
    Return the best combination possible based
    on the budget
    """
    best_portfolio = None
    max_rep = get_max_amount_of_items(items, budget, reverse=False)
    min_rep = get_max_amount_of_items(items, budget)
    for index, combination in enumerate(find_next_combination(items,
                                                              min_rep,
                                                              max_rep)):
        portfolio = Portfolio(combination)
        if index == 0:
            best_portfolio = portfolio
        if portfolio > best_portfolio and portfolio.price < budget:
            best_portfolio = portfolio
        else:
            continue

    print("------------------------------")
    print("{0:>10} {1:>10}   {2}".format("Cout", "Profit", "Portfolio"))
    print(best_portfolio)
    return best_portfolio
