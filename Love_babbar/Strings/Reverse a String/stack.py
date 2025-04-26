# Time Complexity: O(n) 
# Auxiliary Space: O(n)
def reverseString(str):
    stack = []
    for char in str:
        stack.append(char)

    rev = ['']* len(str)

    for i in range(len(str)):
        rev[i] = stack.pop()

    return ''.join(rev) 

if __name__ == "__main__":
    print(reverseString("Mariyam Rahman Wafia"))