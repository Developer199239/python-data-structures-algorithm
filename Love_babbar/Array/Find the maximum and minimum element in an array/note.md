## Problem: Find Minimum and Maximum of an Array with Minimum Comparisons
```bash
arr  = {3, 5, 4, 1, 9}
max: 9 
min: 1
```

we can solve this problem using two method.

## Method 1: The Simple (Naïve) Way
 - Start with the first element as min and max.
 - For every other element:
    - Compare it with min
    - Compare it with max 
 That means 2 comparisons for every element (except the first).   

```bash
Total comparisons = 2 × (n - 1)
```
Example: if n = 6,
comparisons = 2 × 5 = 10

## Method 1: The Smarter Way (Pairwise / Tournament Method)
Instead of comparing each element twice,we can compare elements in pairs — that saves some comparisons.

# How it works
Take elements two at a time (like friends in pairs):
```bash
(arr[0], arr[1]), (arr[2], arr[3]), (arr[4], arr[5]) ...
```
For each pair:
- Compare the two numbers with each other first → (1 comparison)    
    - we now know which one is smaller and which one is larger.
- Compare the smaller one with current min → (1 comparison)
- Compare the larger one with current max → (1 comparison)

So total for one pair = 3 comparisons.

Let’s do a small example
Array: [3, 5, 4, 1, 9, 2]

| Step | Pair      | Internal Compare | min compare | max compare | Total             |
| ---- | --------- | ---------------- | ----------- | ----------- | ----------------- |
| 1    | (3,5)     | 1                | 1           | 1           | 3                 |
| 2    | (4,1)     | 1                | 1           | 1           | 3                 |
| 3    | (9,2)     | 1                | 1           | 1           | 3                 |
|      | **Total** |                  |             |             | **9 comparisons** |

# Compare with naïve way
```bash
For n = 6:
Naïve = 2(n - 1) = 10 comparisons

Pairwise = 3 × (n / 2) = 9 comparisons

we already saved 1 comparison.

```

# Why 3n/2 - 2

*Let’s do a little math*
- we do 3 comparisons for every 2 elements → (3/2) × n = 1.5n comparisons.
- But at the start, we compare the first 2 elements once to initialize min and max.
So we save 2 comparisons there.

*Final Formula:*
```bash
Total comparisons = 3n/2 - 2

If n = 6
3n/2 - 2 = (3×6)/2 - 2 = 9 - 2 = 7 comparisons
```

## comparison table
# method 1
| Step | Element | Compare with min | Compare with max | Comparisons this step | min | max |
| ---- | ------- | ---------------- | ---------------- | --------------------- | --- | --- |
| Init | 3       | —                | —                | 0                     | 3   | 3   |
| 1    | 5       | 5 < 3 ❌          | 5 > 3 ✅          | 2                     | 3   | 5   |
| 2    | 4       | 4 < 3 ❌          | 4 > 5 ❌          | 2                     | 3   | 5   |
| 3    | 1       | 1 < 3 ✅          | 1 > 5 ❌          | 2                     | 1   | 5   |
| 4    | 9       | 9 < 1 ❌          | 9 > 5 ✅          | 2                     | 1   | 9   |

so Total Comparisons = 2 × (n - 1) = 2 × 4 = 8 comparisons

# method 2:
| Step      | Pair   | Pair Comparison | small | large | Compare with min | Compare with max | min   | max   | Comparisons       |
| --------- | ------ | --------------- | ----- | ----- | ---------------- | ---------------- | ----- | ----- | ----------------- |
| Init      | —      | —               | —     | —     | —                | —                | 3     | 3     | 0                 |
| 1         | (5, 4) | 5 > 4 ✅         | 4     | 5     | 4 < 3 ❌          | 5 > 3 ✅          | 3     | 5     | 3                 |
| 2         | (1, 9) | 1 < 9 ✅         | 1     | 9     | 1 < 3 ✅          | 9 > 5 ✅          | 1     | 9     | 3                 |
| **Total** | —      | —               | —     | —     | —                | —                | **1** | **9** | **6 comparisons** |


## Simple Summary for Viva
| Approach             | Description                                 | Comparisons | Time | Space |
| -------------------- | ------------------------------------------- | ----------- | ---- | ----- |
| Naïve                | Compare each element twice (with min & max) | 2(n - 1)    | O(n) | O(1)  |
| Optimized (Pairwise) | Compare in pairs, then update min & max     | 3n/2 - 2    | O(n) | O(1)  |

| Question                                            | Answer                                                                                 |
| --------------------------------------------------- | -------------------------------------------------------------------------------------- |
| What is the minimum number of comparisons required? | 3n/2 - 2                                                                               |
| Why does the pairwise method use fewer comparisons? | Because it compares elements in pairs and uses 3 comparisons per 2 elements.           |
| What is the time complexity?                        | O(n)                                                                                   |
| What is the space complexity?                       | O(1)                                                                                   |
| What happens if the array length is odd?            | First element becomes both min and max, and remaining elements are processed in pairs. |


