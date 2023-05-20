import itertools
import random


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


def random_hill_climbing(items: list[Item], iterations: int = 1000):
    # Init knapsack
    knapsack = Knapsack()
    knapsack.add_items(items)
    permutations = list(itertools.permutations(items))
    # print(permutations[:100])
    random.shuffle(permutations)
    # print(permutations[:100])
    # exit()


    for i in range(iterations):
        new_knapsack = Knapsack()
        new_knapsack.add_items(permutations[i])
        random_knapsack_history.append({
            'id': i,
            'value': new_knapsack.get_total_value(),
        })

        if new_knapsack.get_total_value() > knapsack.get_total_value():
            knapsack = new_knapsack
            random_chosen_knapsack.append(id(new_knapsack))

    return knapsack


def hill_climbing(items: list[Item], iterations: int = 1000):
    # Init knapsack
    knapsack = Knapsack()
    knapsack.add_items(items)

    for i in range(iterations):
        for neighbour_items in get_neighbours(items):
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
    Item(3.9, 3.8),
    Item(3.9, 1.6),
    Item(4.0, 1.1),
    Item(3.2, 4.3),
    Item(2.3, 4.1),
    Item(2.4, 1.7),
    Item(4.0, 4.6),
    Item(4.0, 1.4),
    Item(3.6, 3.3),
    Item(1.1, 1.5),
]

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
def get_all_possible_solutions():
    permutations = list(itertools.permutations(items))
    random.shuffle(permutations)
    possible_solutions = {}

    for permutation in permutations:
        knapsack = Knapsack()
        knapsack.add_items(permutation)
        index_name = ""
        for item in permutation:
            index_name += str(item.weight)
            index_name += ","
        possible_solutions[index_name] = knapsack.get_total_value()

    return possible_solutions


# possible_solutions = get_all_possible_solutions()

# values = list(dict(list(possible_solutions.items())[:100]).values())

# Animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i, vl, period):
    vl.set_xdata(random.randint(0, 99))
    return vl,


def make_animation(title: str, knapsacks, chosen_kanpsacks):
    duration = 30
    refreshPeriod = 300
    plt.title(title)
    plt.ylabel('Solution value')
    plt.xlabel('Permutations')
    plt.xticks([])
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 5)
    line = ax.axvline(0, ls='-', color='r', lw=1, zorder=10)
    x = [sub['id'] for sub in knapsacks]
    print(x)
    y = [sub['value'] for sub in knapsacks]
    print(y)
    ax.plot(x, y)

    ani = animation.FuncAnimation(fig, animate, frames=int(duration / (refreshPeriod / 1000)),
                                  fargs=(line, refreshPeriod),
                                  interval=refreshPeriod)
    ani.save('test.gif')


random_hill_climbing(items)
make_animation("Random hill climbing", random_knapsack_history, random_chosen_knapsack)
