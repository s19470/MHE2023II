import random
import matplotlib.pyplot as plt

# Define the knapsack problem instance
weights = [4.7, 3.9, 2.7, 3.3, 2.6, 1.6, 1.9, 2.2, 1.9, 2.1]  # List of weights of each item
values = [2, 1.8, 2.1, 4.4, 4.8, 1.8, 4.3, 2.4, 4.4, 4.7]  # List of values of each item
max_weight = 15  # Maximum weight capacity of the knapsack

# Initialize the figure and axis for the plot
fig, ax = plt.subplots()
plt.ion()  # Turn on interactive mode

# Create empty lists to store the best value and iteration number at each step
solution_values = []
iterations = []


# Function to calculate the value of a solution
def calculate_value(solution):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += values[i]
            total_weight += weights[i]
    if total_weight > max_weight:
        total_value = 0
    return total_value


# Function to update the plot
def update_plot(solution_values, iterations):
    ax.clear()
    ax.plot(iterations, solution_values)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Best Value')
    plt.pause(0.01)


# Simulated annealing algorithm
def random_hill_climbing(alg_iterations: int = 1000):
    # Initialize the current solution randomly
    current_solution = [random.randint(0, 1) for _ in range(len(weights))]
    best_solution = current_solution.copy()
    current_value = calculate_value(current_solution)
    solution_value = current_value

    for i in range(alg_iterations):
        random_solution = [random.randint(0, 1) for _ in range(len(weights))]
        random_solution_value = calculate_value(random_solution)
        # Accept the neighbor solution if greater
        if random_solution_value >= current_value:
            current_value = random_solution_value
            solution_value = current_value

            # Append the best value and iteration number to the lists
        solution_values.append(solution_value)
        iterations.append(len(solution_values))

        # Update the plot
        update_plot(solution_values, iterations)

    return best_solution, solution_value


# Run the simulated annealing algorithm
solutions, solution_value = random_hill_climbing()

print("Hill climbing solution value:", solution_value)

# Keep the plot window open until it's closed manually
plt.ioff()
plt.show()
