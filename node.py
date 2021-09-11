class Node:
    def __init__(self, x):
        self._name = x
        self.next = None

    def set_next(self, n):
        self.next = n

    def get_next(self):
        return self.next

    def get_name(self):
        return self._name


class Camp:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price
