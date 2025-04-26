# Time Complexity: O(n) 
# Auxiliary Space: O(n)

def reverseStringRecursive(strArr, start, end):
    if start >= end:
        return
    
    strArr[start], strArr[end] = strArr[end], strArr[start]

    reverseStringRecursive(strArr, start+1, end-1)
    

def reverseString(str):
    start = 0
    end = len(str) - 1
    str = list(str)
    
    reverseStringRecursive(str, start, end)

    return ''.join(str)

if __name__ == "__main__":
    print(reverseString("Mariyam Rahman Wafia"))