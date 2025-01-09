################################################################################
# Name: Jugal Patel
# Student ID: 100744586
# Date: 11/10/2024
# Description: This is the main file for Greedy Algorithm Activity
################################################################################

# Part 1:
'''
 The following table shows the weights and values of different items. Assume that we have a knapsack that can hold weight
  weight W = 25, what is the maximum value you may have in the knapsack? you can break the items:
  
  item weight value
  1     5      $20
  2     15     $45
  3     10     $15
  4     6      $12
  '''

items = [(5, 20), (15, 45), (10, 15), (6, 12)]
W = 25

items = [(item[0], item[1], item[1] / item[0]) for item in items]

items = sorted(items, key=lambda x: x[2], reverse=True)

total_value = 0

for item in items:
    if item[0] <= W:
        total_value += item[1]
        W -= item[0]
    else:
        total_value += item[2] * W
        break

print(f"The maximum value you may have in the knapsack is: {total_value}")

# Part C:
'''
Implement (e.g. using python) a greedy algorithm to solve the fractional knapsack problem.
Your program should print a percentage (0.0-1.0) for each item(s) to include in your knapsack
such that weight capacity (W) is not exceeded, and the total value (V, the sum of the value of all included items)
is maximal.

Hint: One way that you could implement this problem is to pass 2 arrays into your procedure:
 1. Weights, where weights[i] is the weight of the element i.
 2. values, where [i] is the value of the element i.
 '''

def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio for each item
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(weights))]
    
    items = sorted(items, key=lambda x: x[2], reverse=True)
    
    total_value = 0  
    fractions = [0] * len(weights)  

    for i, (value, weight, ratio) in enumerate(items):
        if capacity >= weight:

            total_value += value
            capacity -= weight
            fractions[i] = 1.0
        else:

            fraction = capacity / weight
            total_value += value * fraction
            fractions[i] = fraction
            break  

    print("Fractions of items included:", fractions)
    print("Total value of the knapsack:", total_value)

    return fractions, total_value

weights = [5, 15, 10, 6]
values = [20, 45, 15, 12]
capacity = 25

fractional_knapsack(weights, values, capacity)
