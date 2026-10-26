def choice_sort(data: list[float]):
    n = len(data)
    for a in range(n - 1):
        min_num = data[a]
        min_index = a
        for b in range(a + 1, n):
            if data[b] < min_num:
                min_num = data[b]
                min_index = b
        if min_index != a:
            memory = data[a]
            data[a] = data[min_index]
            data[min_index] = memory
    return data


def bingo_sort(data: list[float]):
    max_index = len(data) - 1
    next_value = data[max_index]
    for i in range(max_index - 1, -1, -1):
        if data[i] > next_value:
            next_value = data[i]
    while max_index and data[max_index] == next_value:
        max_index -= 1
    while max_index:
        value = next_value
        next_value = data[max_index]
        for i in range(max_index - 1, -1, -1):
            if data[i] == value:
                data[i], data[max_index] = data[max_index], data[i]
                max_index -= 1
            elif data[i] > next_value:
                next_value = data[i]
        while max_index and data[max_index] == next_value:
            max_index -= 1
    return data


def pancake_sort(data: list[float]):
    n = len(data)
    if n > 1:
        for size in range(n, 1, -1):
            max_index = max(range(size), key=data.__getitem__)
            if max_index + 1 != size:
                if max_index != 0:
                    data[:max_index + 1] = reversed(data[:max_index + 1])
                data[:size] = reversed(data[:size])
    return data


def insert_sort(data: list[float]):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
    return data


def insert_binary_sort(data: list[float]):
    n = len(data)
    for i in range(1, n):
        memory = data[i]
        low, high = 0, i - 1
        while low <= high:
            mid = (low + high) // 2
            if memory < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            data[j] = data[j - 1]
        data[low] = memory
    return data


def merge_list(data1: list[float], data2: list[float]):
    result = []
    i = 0
    j = 0
    while i < len(data1) and j < len(data2):
        if data1[i] <= data2[j]:
            result.append(data1[i])
            i += 1
        else:
            result.append(data2[j])
            j += 1
    result += data1[i:] + data2[j:]
    return result


def merge_sort(data: list[float]):
    n = len(data) // 2
    data1 = data[:n]
    data2 = data[n:]
    if len(data1) > 1:
        data1 = merge_sort(data1)
    if len(data2) > 1:
        data2 = merge_sort(data2)
    return merge_list(data1,data2)

dataset = [541, 934, 661, -868, 709, -277, 142, 493, 286, 733, -229, 79, -190, 493, -85, 799, 997, 751, 439, 946]
dataset2 = [8, 7, 87, 87, 87, 87, 87, 85, 64, 534, 78, 87, 87, 87]
dataset3 = [-2, -8, 9, 1, -1, 0, 6]
sort1 = choice_sort(dataset.copy())
print(sort1)
sort2 = bingo_sort(dataset2.copy())
print(sort2)
sort3 = pancake_sort(dataset2.copy())
print(sort3)
sort4 = insert_sort(dataset.copy())
print(sort4)
sort5 = insert_binary_sort(dataset.copy())
print(sort5)
sort6 = merge_sort(dataset3.copy())
print(sort6)
