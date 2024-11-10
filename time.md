### 1. **Array Operations**
   - **Access (by index)**: O(1) — Direct access to an element by index is constant time.
   - **Search**: O(n) — In an unsorted array, finding an element may require scanning all elements.
   - **Insert/Delete at End**: O(1) — Adding or removing the last element is constant time.
   - **Insert/Delete at Beginning or Middle**: O(n) — Requires shifting elements, which takes linear time.

### 2. **Linked List Operations**
   - **Access (by index)**: O(n) — Accessing a specific index requires traversing the list.
   - **Insert/Delete at Beginning**: O(1) — Adding or removing the first node is constant time.
   - **Insert/Delete at End**: O(n) — In a singly linked list, you may need to traverse to the end.
   - **Search**: O(n) — Requires traversing nodes to find an element.

### 3. **Stack Operations (LIFO)**
   - **Push (add)**: O(1) — Adds to the top of the stack, constant time.
   - **Pop (remove)**: O(1) — Removes the top element, constant time.
   - **Peek (top element)**: O(1) — Checks the top without removal, constant time.
   - **Search**: O(n) — Requires scanning each item.

### 4. **Queue Operations (FIFO)**
   - **Enqueue (add)**: O(1) — Adds to the back, constant time.
   - **Dequeue (remove)**: O(1) — Removes from the front, constant time.
   - **Peek (front element)**: O(1) — Checks the front without removal, constant time.
   - **Search**: O(n) — Requires scanning each item.

### 5. **Hash Table Operations**
   - **Insert/Delete/Search**: O(1) average, O(n) worst-case — Generally, inserting, deleting, and searching are O(1) with a good hash function. However, in the worst case (e.g., all keys hash to the same bucket), they can be O(n).

### 6. **Binary Search Tree (BST) Operations**
   - **Insert/Delete/Search**: O(log n) average, O(n) worst-case — If balanced, these operations are O(log n), but if unbalanced (like a linked list), they degrade to O(n).

### 7. **Sorting Algorithms**
   - **Quick Sort**: O(n log n) average, O(n²) worst-case — Efficient for large datasets on average, but worst case occurs with poor pivot choices.
   - **Merge Sort**: O(n log n) — Consistently O(n log n) for all cases, but requires additional space.
   - **Bubble Sort**: O(n²) — Inefficient for large datasets; compares each pair multiple times.

### 8. **Graph Operations**
   - **Breadth-First Search (BFS) / Depth-First Search (DFS)**: O(V + E) — V is the number of vertices, and E is the number of edges. Traverses each node and edge once.
   - **Dijkstra’s Algorithm**: O((V + E) log V) — Finds the shortest path with a priority queue; more efficient for sparse graphs.

### Summary
- **Constant Time (O(1))**: Fastest, used for direct access, top operations in stacks/queues, or hash table insertions.
- **Logarithmic Time (O(log n))**: Efficient, common in binary trees and binary search.
- **Linear Time (O(n))**: Scans each element once; seen in searches on unsorted structures.
- **Quadratic Time (O(n²))**: Slow, typical in nested loops or simple sorts (like Bubble Sort).
- **Exponential Time (O(2ⁿ))**: Very slow, often in recursive algorithms that branch heavily (e.g., subsets, combinations).

Each scenario depends on the data structure, the type of operation, and any underlying algorithms or optimizations.