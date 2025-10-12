## Idea: Swap the first and last element, then recursively reverse the subarray.
## complexity: O(n) time, O(n) space
## input arr = [1, 4, 3, 2, 6, 5] output: [5, 6, 2, 3, 4, 1]



def reverse_array_recursive(arr, start, end):
    if start >  end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    start = start + 1
    end = end - 1
    reverse_array_recursive(arr, start, end )
    

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6]
    reverse_array_recursive(arr, 0, len(arr) - 1)
    print(arr)