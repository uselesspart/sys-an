import numpy as np


def calculate_probabilities(freq_matrix):
    probabilities = []
    n = len(freq_matrix[0])
    for row in freq_matrix:
        result = [cell / n for cell in row]
        probabilities.append(result)
    return probabilities


def calculate_entropies(freq_matrix):
    prob_matrix = calculate_probabilities(freq_matrix)
    entropy_matrix = [[0] * len(freq_matrix[0]) for _ in range(len(freq_matrix))]
    for i, row in enumerate(prob_matrix):
        for j, prob in enumerate(row):
            entropy = 0
            if prob != 0:
                entropy = -prob * np.log2(prob)
            entropy_matrix[i][j] = entropy
    return entropy_matrix


def calculate_Ha(freq_matrix):
    prob_matrix = calculate_probabilities(freq_matrix)
    entropy_sum = 0
    for row in prob_matrix:
        p = np.sum(row)
        entropy_sum -= p * np.log2(p)
    return entropy_sum


def calculate_Hb(freq_matrix):
    prob_matrix = calculate_probabilities(freq_matrix)
    entropy_sum = 0
    prob_matrix_T = np.transpose(prob_matrix)
    for row in prob_matrix_T:
        p = np.sum(row)
        if p != 0:
            entropy_sum -= p * np.log2(p)
    return entropy_sum


def calculate_HAB(freq_matrix):
    return np.sum(calculate_entropies(freq_matrix))


def task():
    matrix = [[0] * 36 for _ in range(2, 13)]

    for first_dice in range(1, 7):
        for second_dice in range(first_dice, 7):
            matrix[first_dice + second_dice - 2][first_dice * second_dice - 1] += 1 + int(first_dice != second_dice)
    entropy_A = calculate_Ha(matrix)
    entropy_B = calculate_Hb(matrix)
    entropy_AB = calculate_HAB(matrix)
    entropy_A_given_B = entropy_AB - entropy_A
    mutual_information = entropy_B - entropy_A_given_B
    return entropy_AB, entropy_A, entropy_B, entropy_A_given_B, mutual_information


if __name__ == "__main__":
    print(task())
