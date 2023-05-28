import random
import math
import matplotlib.pyplot as plt

# Define the knapsack problem instance
weights = [4.7, 3.9, 2.7, 3.3, 2.6, 1.6, 1.9, 2.2, 1.9, 2.1]  # List of weights of each item
values = [2, 1.8, 2.1, 4.4, 4.8, 1.8, 4.3, 2.4, 4.4, 4.7]  # List of values of each item
max_weight = 15  # Maximum weight capacity of the knapsack

# Define the parameters for simulated annealing
initial_temperature = 100  # Initial temperature
cooling_rate = 0.98  # Cooling rate
iterations_per_temperature = 1

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


# Function to generate a random neighbor solution
def get_neighbor(solution):
    neighbor = solution.copy()
    # Try to avoid neighbor with value 0
    for i in range(len(neighbor) - 1):
        index = random.randint(0, len(neighbor) - 1)
        neighbor[index] = 1 - neighbor[index]  # Flip the bit
        if calculate_value(neighbor) > 0:
            break
    return neighbor


# Function to update the plot
def update_plot(solution_values, iterations):
    ax.clear()
    ax.plot(iterations, solution_values)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Best Value')
    plt.pause(0.01)


# Simulated annealing algorithm
def simulated_annealing():
    # Initialize the current solution randomly
    current_solution = [random.randint(0, 1) for _ in range(len(weights))]
    best_solution = current_solution.copy()
    current_value = calculate_value(current_solution)
    solution_value = current_value

    temperature = initial_temperature

    while temperature > 1:
        for _ in range(iterations_per_temperature):
            # Generate a neighbor solution
            neighbor_solution = get_neighbor(current_solution)
            neighbor_value = calculate_value(neighbor_solution)

            # Calculate the acceptance probability
            acceptance_probability = math.exp((neighbor_value - current_value) / temperature)

            # Accept the neighbor solution with a probability
            if neighbor_value > current_value or random.random() < acceptance_probability:
                current_solution = neighbor_solution
                current_value = neighbor_value
                solution_value = current_value

            # Append the best value and iteration number to the lists
            solution_values.append(solution_value)
            iterations.append(len(solution_values))

            # Update the plot
            update_plot(solution_values, iterations)

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, solution_value


# Run the simulated annealing algorithm
best_solution, solution_value = simulated_annealing()

print("Simulated annealing solution value:", solution_value)
print(len(iterations))

# Plot the final result
update_plot(solution_values, iterations)

# Keep the plot window open until it's closed manually
plt.ioff()
plt.show()
