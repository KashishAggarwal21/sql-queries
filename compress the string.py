from itertools import groupby

# Read input
s = input()

# Apply groupby and build the result
result = [(len(list(group)), int(key)) for key, group in groupby(s)]

# Print output in the required format
print(' '.join(str(t) for t in result))
