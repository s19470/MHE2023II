import itertools
import random
import string
import math


class Item:
    def __init__(self, value: float, weight: float):
        self.value = value
        self.weight = weight

    def goal(self):
        return self.value / self.weight


class Knapsack:
    def __init__(self, max_weight: float = 15):
        self.max_weight = max_weight
        self.items: list[Item] = []

    def add_item(self, item: Item):
        if self.get_total_weight() + item.weight > self.max_weight:
            return False

        self.items.append(item)
        return True

    def add_items(self, items: list[Item]):
        self.memory_items = items
        for item in items:
            self.add_item(item)

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


# Stochastic hill climbing
random_knapsack_history = []
random_chosen_knapsack = []


def random_hill_climbing(items: list[Item], iterations: int = 100):
    # Init knapsack
    knapsack = Knapsack()
    knapsack.add_items(items)
    permutations = list(itertools.permutations(items))
    random.shuffle(permutations)

    for i in range(iterations):
        new_knapsack = Knapsack()
        new_knapsack.add_items(permutations[i])
        name = ''.join(random.sample(string.ascii_lowercase, 10))
        random_knapsack_history.append({
            'id': name,
            'value': new_knapsack.get_total_value(),
        })

        if new_knapsack.get_total_value() > knapsack.get_total_value():
            knapsack = new_knapsack
            random_chosen_knapsack.append(name)

    return knapsack


basic_knapsack_history = []
basic_chosen_knapsack = []


def hill_climbing(items: list[Item], iterations: int = 100):
    # Init knapsack
    knapsack = Knapsack()
    knapsack.add_items(items)

    for i in range(iterations):
        for neighbour_items in get_neighbours(knapsack.memory_items):
            new_knapsack = Knapsack()
            new_knapsack.add_items(neighbour_items)
            if new_knapsack.get_total_value() > knapsack.get_total_value():
                knapsack = new_knapsack

    return knapsack


def get_neighbours(items):
    neighbours = []

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            neighbour = items.copy()
            neighbour[i] = items[j]
            neighbour[j] = items[i]
            neighbours.append(neighbour)

    return neighbours


items = [
    Item(4.7, 2.0),
    Item(3.9, 1.8),
    Item(2.7, 2.1),
    Item(3.3, 4.4),
    Item(2.6, 4.8),
    Item(1.6, 1.8),
    Item(1.9, 4.3),
    Item(2.2, 2.4),
    Item(1.9, 4.4),
    Item(2.1, 4.7),
]

# items = [
#     Item(4.7, 2.0),
#     Item(3.9, 1.8),
#     Item(2.7, 2.1),
#     Item(3.3, 4.4),
#     Item(2.6, 4.8),
#     Item(1.6, 1.8),
#     Item(10, 4.3),
#     Item(2.2, 2.4),
#     Item(1.9, 4.4),
#     Item(8, 4.7),
# ]

random.shuffle(items)

for item in items:
    print("Value: ", item.value, "Weight: ", item.weight, "Goal: ", item.goal())

# print("Random hill climbing")
# knapsack = random_hill_climbing(items)
# knapsack.print_items()
# print("Random hill climbing total value:", knapsack.get_total_value())
#
# print("Hill climbing")
# knapsack = hill_climbing(items)
# knapsack.print_items()
# print("Hill climbing total value:", knapsack.get_total_value())


# Chart animations
# def get_all_possible_solutions():
#     permutations = list(itertools.permutations(items))
#     random.shuffle(permutations)
#     possible_solutions = {}
#
#     for permutation in permutations:
#         knapsack = Knapsack()
#         knapsack.add_items(permutation)
#         index_name = ""
#         for item in permutation:
#             index_name += str(item.weight)
#             index_name += ","
#         possible_solutions[index_name] = knapsack.get_total_value()
#
#     return possible_solutions
#
#
# # Animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#
#
def animate(i, vl, chosen_knapsacks):
    vl.set_color('b')
    vl.set_xdata(chosen_knapsacks[i])
    return vl,


def make_animation(title: str, knapsacks, chosen_knapsacks):
    refreshPeriod = 100
    fig, ax = plt.subplots()
    ax.set_ylabel('Solution value')
    ax.set_xlabel('Permutations')
    ax.set_xticks([])
    ax.set_title(title)

    fig.set_size_inches(20, 5)
    line = ax.axvline(0, ls='-', color='r', lw=1, zorder=10)
    random.shuffle(knapsacks)
    x = [sub['id'] for sub in knapsacks]
    y = [sub['value'] for sub in knapsacks]
    ax.plot(x, y)
    ani = animation.FuncAnimation(fig, animate, frames=len(chosen_knapsacks),
                                  fargs=(line, chosen_knapsacks),
                                  interval=refreshPeriod)
    ani.save(title + '.gif')

#
# random_hill_climbing(items)
# make_animation("Random hill climbing", random_knapsack_history, random_chosen_knapsack)


simulated_knapsack_history = []
simulated_chosen_knapsack = []


def simulated_annealing(items: list[Item], temperature: float = 30, cooling_rate: float = .95):
    knapsack = Knapsack()
    knapsack.add_items(items)

    while temperature > 1:
        new_knapsack = Knapsack()
        new_knapsack.add_items(random.choice(get_neighbours(knapsack.memory_items)))

        # Animation
        name = ''.join(random.sample(string.ascii_lowercase, 10))
        simulated_knapsack_history.append({
            'id': name,
            'value': new_knapsack.get_total_value(),
        })

        # print(random.uniform(0, 1) < math.exp((knapsack.get_total_value() - new_knapsack.get_total_value()) / temperature))

        if new_knapsack.get_total_value() >= knapsack.get_total_value():
            knapsack = new_knapsack
            # Animation
            simulated_chosen_knapsack.append(name)
            # print(new_knapsack.print_items())

        # D(1,2) < E^(value diff / temperature).
        elif random.uniform(0, 1) < math.exp((new_knapsack.get_total_value() - knapsack.get_total_value()) / temperature):
            print(math.exp((new_knapsack.get_total_value() - knapsack.get_total_value()) / temperature))
            knapsack = new_knapsack
            # Animation
            simulated_chosen_knapsack.append(name)

        else:
            pass
            # print("dupa")
            # exit()

        temperature *= cooling_rate

    return knapsack


print("Simulated annealing")
knapsack = simulated_annealing(items)
knapsack.print_items()
print("Simulated annealing total value:", knapsack.get_total_value())

make_animation("Simulated annealing climbing", simulated_knapsack_history, simulated_chosen_knapsack)

print(len(simulated_chosen_knapsack))

# print("Random hill climbing")
# knapsack = random_hill_climbing(items)
# knapsack.print_items()
# print("Random hill climbing total value:", knapsack.get_total_value())
