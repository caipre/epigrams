#!/usr/bin/env python3

def calculate_number_of_score_combinations(scores, target):
    combinations = [0 for _ in range(target + 1)]
    combinations[0] = 1
    for score in scores:
        for j in range(score, len(combinations)):
            combinations[j] += combinations[j - score]
    return combinations[target]

scores = (2, 3, 7)
target = 12
print(calculate_number_of_score_combinations(scores, target))
