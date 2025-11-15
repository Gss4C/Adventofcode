import pandas as pd

#### PART 1 ####
df = pd.read_table("./input.txt", sep= "   ", header=None)
A = df[0].sort_values()
B = df[1].sort_values()
total_distance = 0
for a, b in zip(A, B):
    total_distance += abs(a - b)
print("Total distance: " , total_distance)

#### PART 2 ####
B_freq = B.value_counts().to_dict()
total_similarity = 0
for elemento_a in A:
    #similarity = elemento_a * B_freq.get(elemento_a, 0)
    total_similarity += elemento_a * B_freq.get(elemento_a, 0)

print('Total similarity: ', total_similarity)