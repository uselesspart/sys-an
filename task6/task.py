import numpy as np

def extract_clusters(data_string):
    data_string = str(data_string[1:-1])
    data_split = data_string.split(",")
    clusters = []
    in_cluster = False
    for substring in data_split:
        current_cluster = in_cluster
        if '[' in substring:
            substring = substring[1:]
            in_cluster = True
        if ']' in substring:
            substring = substring[:-1]
            in_cluster = False

        if not current_cluster:
            clusters.append([int(substring)])
        else:
            clusters[-1].append(int(substring))
    return clusters

def generate_matrix_from_expert(data_str: str):
    matrix = []
    n = 0

    clusters = extract_clusters(data_str)
    for cluster in clusters:
        n += len(cluster)
    for i in range(n):
        matrix.append([1] * n)

    exclusion_list = []
    for cluster in clusters:
        for excluded_elem in exclusion_list:
            for elem in cluster:
                matrix[elem - 1][excluded_elem - 1] = 0
        for elem in cluster:
            exclusion_list.append(int(elem))

    return np.array(matrix)

def calculate_kendell_similarity(experts):
    m = len(experts)
    n = len(experts[0])

    rank_matrix = [[0 for _ in range(len(experts))] for _ in range(len(experts[0]))]
    for i, expert in enumerate(experts):
        for j, obj in enumerate(expert):
            rank_matrix[j][i] = len(obj) - np.sum(obj) + 1

    H = 0
    for i in range(m):
        d = {}
        for obj in rank_matrix:
            if d.get(obj[i]) is None:
                d[obj[i]] = 0
            d[obj[i]] = d[obj[i]] + 1
        for k in d:
            H += d[k] ** 3 - d[k]
        for j, obj in enumerate(rank_matrix):
            rank_matrix[j][i] = rank_matrix[j][i] + (d[obj[i]] - 1) / 2

    Xmean = np.sum(rank_matrix) / n

    S = 0
    for obj_ranks in rank_matrix:
        Xi = np.sum(obj_ranks)
        S += (Xi - Xmean) ** 2

    Dmax = (m * m * (n ** 3 - n) - m * H) / 12

    return S / Dmax

def task(str_a: str, str_b: str):
    matrix_f = generate_matrix_from_expert(str_a)
    matrix_g = generate_matrix_from_expert(str_b)
    experts = [matrix_g, matrix_f]
    similarity = calculate_kendell_similarity(experts)
    return similarity

if __name__ == "__main__":
    print(
        task(
            "[1,[2,3],4,[5,6,7],8,9,10]",
            "[[1,2],[3,4,5],6,7,9,[8,10]]"
        )
    )
