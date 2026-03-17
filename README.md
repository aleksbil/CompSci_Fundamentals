## Algorithm Efficiency Showcase: Sorting & Searching

This project provides an interactive demonstration of fundamental computer science algorithms, focusing on the trade-offs between different time complexities. As a Data Analyst, I built this to visualize how data structure and algorithm choice impact performance.

### Core Concepts
The script implements and visualizes:
1.  **Bubble Sort**: A foundational sorting algorithm ($O(n^2)$) used here to prepare the dataset for efficient searching.
2.  **Binary Search**: A "Divide and Conquer" algorithm ($O(\log n)$) that drastically reduces search time for large datasets.
3.  **Linear Search**: A baseline comparison ($O(n)$) to demonstrate real-world efficiency gains.

### Key Features
- **Robust Input Validation**: Includes a `try-except` engine that handles faulty user inputs (letters, empty strings, etc.), ensuring a smooth user experience.
- **Visual Process Logging**: Every swap in the sorting process and every "jump" in the search process is logged to the console, making the abstract logic visible.
- **Fair Performance Battle**: The script compares steps taken by both search methods and declares a winner, acknowledging that Linear Search can be faster for elements near the start of a list.

### Performance Comparison
While Linear Search scales poorly with large data, Binary Search remains incredibly fast.

| Dataset Size | Linear Search (Worst Case) | Binary Search (Worst Case) |
| :--- | :--- | :--- |
| 10 items | 10 steps | ~4 steps |
| 1,000 items | 1,000 steps | ~10 steps |
| 1,000,000 items | 1,000,000 steps | ~20 steps |

### Cognitive Science & HCI Connection
This project explores the intersection of **Human-Computer Interaction (HCI)** and **Cognitive Ecology**. By optimizing search paths, we reduce the computational "energy" required to find information—a principle that mirrors how humans organize their environments to minimize cognitive load.

### How to Run
1. Ensure you have Python 3.x installed.
2. Run the script: `python algorithm_showcase.py`
3. Follow the interactive prompts to enter your numbers and see the algorithms in action!
