import itertools


class Item:
    def __init__(self, value: float, weight: float):
        self.value = value
        self.weight = weight

    def goal(self):
        return self.value / self.weight


class Knapsack:
    # items: list[Item]
    def __init__(self, max_weight: float = 10):
        self.max_weight = max_weight
        self.items: list[Item] = []

    def add_item(self, item: Item):
        if self.get_total_weight() + item.weight > self.max_weight:
            return False

        self.items.append(item)
        return True

    def get_total_weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight
        return weight

    def get_total_value(self):
        value = 0
        for item in self.items:
            value += item.value
        return value

    def print_items(self):
        for item in self.items:
            print("Value: ", item.value, "Weight: ", item.weight)

def hill_climbing(items: list[Item]):




items = [
    Item(1.7, 1.1),
    Item(4.8, 5.5),
    Item(9.2, 1.4),
    Item(0.7, 1.4),
    Item(8.9, 1.6),
    Item(7.5, 8.8),
]

permutations = list(itertools.permutations(items))

knapsack = Knapsack()

for item in items:
    knapsack.add_item(item)

knapsack.print_items()
