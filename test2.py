import random
import math

# Define the knapsack problem instance
weights = [2, 3, 4, 5, 6]  # List of weights of each item
values = [3, 4, 5, 6, 7]   # List of values of each item
max_weight = 10             # Maximum weight capacity of the knapsack

# Define the parameters for simulated annealing
initial_temperature = 100   # Initial temperature
cooling_rate = 0.95         # Cooling rate
iterations_per_temperature = 100

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
    index = random.randint(0, len(neighbor) - 1)
    neighbor[index] = 1 - neighbor[index]  # Flip the bit
    return neighbor

# Simulated annealing algorithm
def simulated_annealing():
    # Initialize the current solution randomly
    current_solution = [random.randint(0, 1) for _ in range(len(weights))]
    best_solution = current_solution.copy()
    current_value = calculate_value(current_solution)
    best_value = current_value

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

            # Update the best solution
            if current_value > best_value:
                best_solution = current_solution.copy()
                best_value = current_value

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, best_value

# Run the simulated annealing algorithm
best_solution, best_value = simulated_annealing()

# Print the best solution and its value
print("Best Solution:", best_solution)
print("Best Value:", best_value)