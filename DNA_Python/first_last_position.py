# Given a sorted array of int "arr" and "t" target, find the index of the
# first and last position of target in arr.

def FnL_position(arr, target):
    sort_arr = sorted(arr)
    print(sort_arr)
    for i in range(len(sort_arr)):
        if sort_arr[i] == target:
            start = i
            while i+1 < len(sort_arr) and sort_arr[i+1]== target:
                i +=1
            return [start, i]
    
    return [-1,-1]
     



list_arr = [1, 2, 5, 7, 8, 99, 7, 56, 4, 6, 45, 7, ]
print(FnL_position(list_arr, 7))
