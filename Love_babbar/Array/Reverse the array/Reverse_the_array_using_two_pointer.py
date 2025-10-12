## Idea: Use two pointers — one at the start and one at the end — and swap elements until they meet.
## complexity: O(n) time, O(1) space
## input arr = [1, 4, 3, 2, 6, 5] output: [5, 6, 2, 3, 4, 1]



def reverseArray(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1
    return arr    

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    print(reverseArray(arr))