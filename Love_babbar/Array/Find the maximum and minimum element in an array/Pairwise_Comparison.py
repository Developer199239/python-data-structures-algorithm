def find_min_max_pairwise(arr):
    n = len(arr)
    if n == 0:
        return 
    min_val = max_val = arr[0]

    if n % 2 == 0:
        if arr[0] < arr[1]:
            min_val = arr[0]
            max_val = arr[1]
        else:
            min_val = arr[1]
            max_val = arr[0]
        start_index = 2    
    else:
        min_val, max_val = arr[0]
        start_index = 1        

    for i in range(start_index,n-1,2):
        if arr[i] < arr[i + 1]:
            small, large = arr[i], arr[i + 1]
        else:
            small, large = arr[i + 1], arr[i]

        if small < min_val:
            min_val = small
        if large > max_val:
            max_val = large        
    
    return min_val, max_val
    

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    min_value,max_value = find_min_max_pairwise(arr)
    print("Min:", min_value, ", Max:", max_value)