import timeit
import random

def insertion_sort(lst):
    arr = lst[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

sorting_functions = [insertion_sort, merge_sort, sorted]
sizes = [10, 100, 1_000, 10_000]
test_data = {n: [random.randint(0, n*10) for _ in range(n)] for n in sizes}

def measure_execution_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data[:]), number=10)

columns = ["Algorithm"] + [f"{n} elements" for n in sizes]
header = "|" + "|".join(f"{col:<20}" for col in columns) + "|"
separator = "|" + "|".join(":" + "-"*19 for _ in columns) + "|"

print(header)
print(separator)

for sort_func in sorting_functions:
    row = f"|{sort_func.__name__:<20}"
    for n in sizes:
        execution_time = measure_execution_time(sort_func, test_data[n])
        row += f"|{execution_time:<20.5f}"
    row += "|"
    print(row)