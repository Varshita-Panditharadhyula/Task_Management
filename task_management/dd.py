#Author: Varshita Panditharadhyula
#Date:26-12-2023
#Project: DIgital Design Project
from itertools import product

# Function to generate truth table for a given number of variables
def generate_truth_table(num_vars):
    inputs = list(product([0, 1], repeat=num_vars))
    return inputs

# Function to display truth table
def display_truth_table(inputs, outputs):
    print("Truth Table:")
    for idx, input_combination in enumerate(inputs):
        print(f"{input_combination} -> {outputs[idx]}")

# Function to simplify a logic function using tabular method
def tabular_method(inputs, outputs):
    minterms = []
    dont_cares = []

    for idx, output in enumerate(outputs):
        if output == 1:
            minterms.append(inputs[idx])
        elif output == 'x':
            dont_cares.append(inputs[idx])

    return minterms, dont_cares

# Example truth table inputs and outputs
inputs = generate_truth_table(3)  # Change the number for different variables
outputs = [0, 1, 0, 1, 1, 'x', 'x', 0]  # Replace this with your own function's outputs

# Display the initial truth table
display_truth_table(inputs, outputs)

# Apply tabular method to simplify logic function
minterms, dont_cares = tabular_method(inputs, outputs)

print("\nMinterms:", minterms)
print("Don't Cares:", dont_cares)
