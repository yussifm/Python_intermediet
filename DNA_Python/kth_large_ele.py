# Given an array of integers arr and an interger k,
# find the 'k'th largest element 


import heapq



def kth_largest(arr, k):
    for i in range(0, k-1):
        arr.remove(max(arr))
    return max(arr)

# second solution using sort

def kth_element(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]


# third solution using heaps and priority queues

def kth_l_heap(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


list_arr = [1, 2, 5, 7, 8, 99, 7, 56, 4, 6, 45, 7, ]
print(kth_element(list_arr, 6))
print(kth_largest(list_arr, 6))