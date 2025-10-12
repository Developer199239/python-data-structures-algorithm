| Question                                  | Short Answer                                            |
| ----------------------------------------- | ------------------------------------------------------- |
| What is the time complexity?              | O(n)                                                    |
| What is the space complexity (iterative)? | O(1)                                                    |
| What is the space complexity (recursive)? | O(n) due to stack                                       |
| Is the two-pointer method in-place?       | Yes                                                     |
| What is a call stack?                     | Memory area that stores function calls during execution |
| Which approach is most efficient?         | Two-pointer (in-place)                                  |
| What is recursion?                        | A function calling itself to solve smaller subproblems  |


## Why recursion uses O(n) space
When you call a function recursively, each function call is stored on the call stack (a special memory area that keeps track of active function calls).

Each call waits for the next one to finish before it can return — so they stack up in memory.

## Why use two-pointer instead of recursion?
Because recursion uses extra stack memory (O(n)), while the two-pointer method is in-place and more memory-efficient (O(1)).