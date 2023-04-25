# The player uses fire to smelt gems. After each smelting, there is a chance to upgrade the fire. The higher the level of the fire, the better the gems that can be smelted.
# The level L, the number of smeltings N, and the guaranteed slot M. When M=30, the guarantee is triggered and L is directly assigned a value of 5.
# The probability of upgrading each time is 0.4. When L=5, the fire will return to level 1 directly after smelting.
# When L=5 and M=30, the guarantee is triggered to directly upgrade to level 5, instead of returning to level 1.

import random
import matplotlib.pyplot as plt

L = 1
M = 0
N = 0

# Store the results of L in a list
level_list = []

# Get the occurrence of each element in the list
def all_list(arr):
  result = {}
  for i in set(arr):
    result[i] = arr.count(i)
  return result

# The smelting process starts

while N<10000:
    if M>= 30:   # When M >= 30, the guarantee is triggered and directly upgraded to level 5 while clearing the guaranteed slot
        L = 5
        M = 0
    else:
        if L==5:   #When L = 5, it fails, and the guaranteed slot accumulates 5
            L = 1
            M = M+5
        else:
            p = random.random()
            # Successful strengthening, level +1, and guaranteed slot increases
            if p < 0.4:
                M = M + L
                L = L+1
            #  Failed strengthening, directly return to level 1, and guaranteed slot increases
            else:
                M = M+L
                L = 1
    N=N+1

    # Store the level L in a list
    level_list.append(L)
    frequency = all_list(level_list)
print(frequency)


# Create a histogram of the data
plt.hist(level_list)

# Set the x-axis tick labels
plt.xticks(range(1, 6))

# Set the chart title and axis labels
plt.title("Distribution of Level")
plt.xlabel("Level")
plt.ylabel("Frequency")

# Show the chart
plt.show()