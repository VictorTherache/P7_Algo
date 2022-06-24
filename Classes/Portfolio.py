
from Classes.Action import Action


class Portfolio:
    """
    A collection of actions with methods
    to add an action to the porfolio, get the
    cost, profit and names of all the actions
    """

    def __init__(self, actions=None, max_price: float = 500):
        self.actions = actions or []
        self.max_price = max_price
        self.__profit = None
        self.__price = None

    def add(self, action: Action):
        """
        Add an action to the portfolio
        """
        if self.price + action.price > self.max_price:
            return False
        self.actions.append(action)            
        return True

    @property
    def price(self):
        """
        Return the total cost of the portfolio
        """
        return sum(x.price for x in self.actions)

    @property
    def profit(self):
        """
        Return the profit of the portfolio
        """
        return round(sum(x.profit for x in self.actions), 2)

    @property
    def names(self):
        """
        Return all the actions name
        """
        return ', '.join([x.name for x in self.actions])

    def __repr__(self):
        """
        Return the string to be shown when printing the class
        """
        return "{0:10}€ {1:10}€   {2}".format(round(self.price, 2),
                                              self.profit,
                                              self.names)

    def __gt__(self, other):
        """
        Compares attribute "x" of objects, self stands for 1st object
        and other stands for object after ">" sign.
        """
        return True if other is None else self.profit > other.profit

    def __len__(self):
        """
        """
        return len(self.actions)