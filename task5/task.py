import numpy as np

# Расширяем список, преобразуя вложенные списки в один плоский список
def expand_list(r_list):
    expanded_ranks = []
    for elem in r_list:
        if isinstance(elem, int):
            expanded_ranks.append(elem)
        else:
            expanded_ranks.extend(elem)
    return sorted(expanded_ranks)

# Создаём матрицу рангов из расширенного списка
def construct_matrix(rank_lst):
    expanded_list = expand_list(rank_lst)
    rank_mtrx = np.zeros(shape=(len(expanded_list), len(expanded_list)), dtype=int)
    for i, val_i in enumerate(expanded_list):
        for j, val_j in enumerate(expanded_list):
            if val_i == val_j or not is_inferior(rank_lst, val_i, val_j):
                rank_mtrx[i, j] = 1
    return rank_mtrx

# Проверяем, является ли один элемент инфериорным по отношению к другому в заданном списке рангов
def is_inferior(rank_lst, first, second):
    for item in rank_lst:
        if isinstance(item, int):
            if first == item:
                return True
            if second == item:
                return False
            continue
        if first in item:
            return second not in item
        if second in item:
            return first in item
    return False

# Собираем итоговый рейтинг на основе спорных пар, представленных в виде списков рангов
def assemble_ranking(disputed_pairs, ranks_1, ranks_2):
    expanded_1 = expand_list(ranks_1)
    expanded_2 = expand_list(ranks_2)
    final_ranking = []

    added_items = set()

    for itm in expanded_1 + expanded_2:
        if itm not in added_items:
            controversy_group = [itm]
            for pair in disputed_pairs:
                if itm in pair:
                    other_item = pair[0] if pair[1] == itm else pair[1]
                    controversy_group.append(other_item)
            
            if len(controversy_group) > 1:
                final_ranking.append(controversy_group)
            else:
                final_ranking.append(itm)
            
            added_items.update(controversy_group)

    return final_ranking

# Задаём функцию для решения задачи
def task(input_1, input_2):
    rank_1 = construct_matrix(input_1)
    rank_2 = construct_matrix(input_2)

    combined_mtrx = np.multiply(rank_1, rank_2)
    transposed_mtrx = np.multiply(np.transpose(rank_1), np.transpose(rank_2))
    dispute_mtrx = np.zeros(rank_1.shape, dtype=int)
    for i in range(len(combined_mtrx)):
        for j in range(len(combined_mtrx[i])):
            dispute_mtrx[i, j] = combined_mtrx[i, j] or transposed_mtrx[i, j]

    disputed_pairs = []
    for i in range(len(dispute_mtrx)):
        for j in range(len(dispute_mtrx[i])):
            if i < j:
                continue
            if dispute_mtrx[i, j] == 0:
                disputed_pairs.append((j + 1, i + 1))

    return assemble_ranking(disputed_pairs, input_1, input_2)

# Входные данные
input_1 = [1, [2, 3], 4, [5, 6, 7], 8, 9, 10]
input_2 = [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]

# Вызываем и печатаем результат функции task
print(task(input_1, input_2))
