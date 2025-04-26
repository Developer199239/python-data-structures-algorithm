# Time Complexity: O(n) 
# Auxiliary Space: O(n)

def reverseString(str):
    start = 0
    end = len(str) - 1

    str = list(str)

    while start < end:
        str[start], str[end] = str[end], str[start]
        start +=1
        end -=1
    
    return ''.join(str)

if __name__ == "__main__":
    print(reverseString("DSA"))