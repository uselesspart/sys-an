import numpy as np

def convert_str_to_clusters(input_str):
    input_str = str(input_str[1:-1])
    split_values = input_str.split(",")
    clusters = []
    cluster_started = False
    for substr in split_values:
        was_cluster_started = cluster_started
        if '[' in substr:
            substr = substr[1:]
            cluster_started = True
        if ']' in substr:
            substr = substr[:-1]
            cluster_started = False

        if not was_cluster_started:
            clusters.append([int(substr)])
        else:
            clusters[-1].append(int(substr))
    return clusters

def convert_str_to_matrix(input_str: str):
    matrix = []
    n = 0

    clusters = convert_str_to_clusters(input_str)
    for cluster in clusters:
        n += len(cluster)
    for i in range(n):
        matrix.append([1] * n)

    excluded = []
    for cluster in clusters:
        for excluded_elem in excluded:
            for elem in cluster:
                matrix[elem - 1][excluded_elem - 1] = 0
        for elem in cluster:
            excluded.append(int(elem))

    return np.array(matrix)

def get_and_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = []
    for row in range(rows):
        result_matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            result_matrix[row][col] = matrix1[row][col] * matrix2[row][col]

    return np.array(result_matrix)

def get_or_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = []
    for row in range(rows):
        result_matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            result_matrix[row][col] = max(matrix1[row][col], matrix2[row][col])

    return result_matrix

def find_clusters(matrix, est1, est2):
    clusters = {}

    rows = len(matrix)
    cols = len(matrix[0])
    exclude=[]
    for row in range(rows):
        if row+1 in exclude:
            continue
        clusters[row + 1] = [row + 1]
        for col in range(row+1, cols):
            if matrix[row][col] == 0:
                clusters[row + 1].append(col + 1)
                exclude.append(col+1)

    result = []
    for k in clusters:
        if not result:
            result.append(clusters[k])
            continue
        for i, elem in enumerate(result):
            if np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1]) and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1]):
                for c in clusters[k]:
                    result[i].append(c)
                    break

            if np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1]) or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1]):
                result = result[:i] + clusters[k] + result[i:]
                break
        result.append(clusters[k])

    final = []
    for r in result:
        if len(r) == 1:
            final.append(r[0])
        else:
            final.append(r)
    return str(final)

def task(input_str1, input_str2):
    matrix1 = convert_str_to_matrix(input_str1)
    matrix2 = convert_str_to_matrix(input_str2)

    and_matrix = get_and_matrix(matrix1, matrix2)
    and_matrix_transposed = get_and_matrix(np.transpose(matrix1), np.transpose(matrix2))

    or_matrix = get_or_matrix(and_matrix, and_matrix_transposed)
    clusters = find_clusters(or_matrix, matrix1, matrix2)
    return clusters

if __name__ == "__main__":
    input_str1 = '[10, 2, 3, 4, 5, 6, 7, 8, 9, 1]'
    input_str2 = '[1, 2, 3, 4, 5, 6, 7, 9, 8, 10]'
    results = task(input_str1, input_str2)
    print(results)
