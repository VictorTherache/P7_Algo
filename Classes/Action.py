from dataclasses import dataclass


@dataclass
class Action:
    """
    Action class with a name, price and relative profit
    Calling the profit method will calculate the profit
    of the action
    """
    name: str
    price: float
    relative_profit: float

    @property
    def profit(self):
        """
        Return the profit of the action
        """
        return self.price * self.relative_profit / 100
