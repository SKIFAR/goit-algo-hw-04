## Conclusion

|Algorithm           |10 elements         |100 elements        |1000 elements       |10000 elements      |
|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|
|insertion_sort      |0.00004             |0.00235             |0.24369             |25.03367            |
|merge_sort          |0.00011             |0.00162             |0.01944             |0.25278             |
|sorted              |0.00001             |0.00006             |0.00111             |0.02071             |

1. **Insertion Sort** performs well only on very small datasets (≤100 elements).  
   Its quadratic time complexity (**O(n²)**) makes it impractical for larger arrays.

2. **Merge Sort** shows stable performance across all dataset sizes with the expected complexity of **O(n log n)**.  
   However, it requires additional memory and is not as optimized as Python’s built-in solution.

3. **Timsort** (used in Python’s `sorted` and `.sort()`) outperforms both algorithms in practice:  
   - It combines **Insertion Sort** (for small runs) and **Merge Sort** (for larger parts).  
   - It adapts to partially sorted data, achieving nearly **O(n)** in the best case.  
   - On average and large datasets, it is consistently faster than pure Merge Sort.

**Key takeaway:**  
In real-world Python applications, developers rely on the built-in `sorted` / `.sort()` functions because Timsort is highly optimized, adaptive, and efficient compared to manually implemented sorting algorithms.