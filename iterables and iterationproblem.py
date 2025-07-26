from itertools import combinations

# Input parsing
n = int(input())
letters = input().split()
k = int(input())

# Total combinations of length k
all_combinations = list(combinations(letters, k))

# Filter combinations where 'a' is present
favorable = [combo for combo in all_combinations if 'a' in combo]

# Compute probability
probability = len(favorable) / len(all_combinations)

# Print result up to 3 decimal places
print(f"{probability:.4f}")
