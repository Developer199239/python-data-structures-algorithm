def find_min_max_naive(arr):
    n = len(arr)
    if n == 0:
        return 
    min_val = max_val = arr[0]

    for i in range(1,n):
        if arr[i] < min_val:
            min_val = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]    
    
    return min_val, max_val
    

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 0]
    min_value,max_value = find_min_max_naive(arr)
    print("Min:", min_value, ", Max:", max_value)