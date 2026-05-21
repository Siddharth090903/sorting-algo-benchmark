import time
import random

# 1. Bubble Sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2. Insertion Sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3. Merge Sort 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 4. Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Benchmarking Function 
def benchmark_algorithms():
    sizes = [100, 500, 1000] # Test with small, medium, and large arrays
    
    print("--- Sorting Algorithm Benchmark Results ---")
    
    for size in sizes:
        print(f"\nArray Size: {size}")
        test_data = [random.randint(1, 10000) for _ in range(size)]
        
        # Benchmark Bubble Sort
        arr_copy = test_data.copy()
        start = time.time()
        bubble_sort(arr_copy)
        print(f"Bubble Sort:    {time.time() - start:.5f} seconds")
        
        # Benchmark Insertion Sort
        arr_copy = test_data.copy()
        start = time.time()
        insertion_sort(arr_copy)
        print(f"Insertion Sort: {time.time() - start:.5f} seconds")
        
        # Benchmark Merge Sort
        arr_copy = test_data.copy()
        start = time.time()
        merge_sort(arr_copy)
        print(f"Merge Sort:     {time.time() - start:.5f} seconds")
        
        # Benchmark Quick Sort
        arr_copy = test_data.copy()
        start = time.time()
        quick_sort(arr_copy)
        print(f"Quick Sort:     {time.time() - start:.5f} seconds")

if __name__ == "__main__":
    benchmark_algorithms()

