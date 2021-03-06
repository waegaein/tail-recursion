# Tail Recursion in Python

## Abstract
Programming should follow the narrative of the problem to solve.
Some fits better into iteration, whereas some fits into recursion.
However, plain recursion is not so great when it comes to performance.
Tail recursion may come here to the rescue.
There is not actually a tail call optimization in Python, nevertheless, the trick here shows performance/resource boost comparable to iteration.

## Installation
1. Clone the repository.
`git clone git@github.com:waegaein/tail-recursion.git`
2. Install the requirements.
`pip install -r requirements.txt`
3. Run the benchmark; Use index as you want for the Fibonacci sequence.
`bash benchmark.sh 20`
4. Play with your own configurations!
`benchmark.sh, main.py, utils.py`

## Sample Output
```
-------------------------
fibonacci_plain_recursive
-------------------------
Result: 10946
Elapsed: 3901.50 msec
Allocated: 11.91 MiB

-------------------
fibonacci_iterative
-------------------
Result: 10946
Elapsed: 4.01 msec
Allocated: 1.56 MiB

------------------------
fibonacci_tail_recursive
------------------------
Result: 10946
Elapsed: 5.37 msec
Allocated: 0.80 MiB
```

## Reference
* Chris, P. (2017, July 26). _Tail Recursion in Python_ [[Link]](https://chrispenner.ca/posts/python-tail-recursion)


