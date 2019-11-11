# Tail Recursion in Python

## Abstract
Programming should follow the narrative of the problem to solve.
Some fits better into iteration, whereas some fits into recursion.
However, plain recursion is not so great when it comes to performance.
Tail recursion may come here to the rescue.
There is not actually a tail call optimization in Python
Nevertheless, tail recursion trick here shows meaningful performance/resource boost at least.

## Installation
1. Clone repository.
`git@github.com:waegaein/tail-recursion.git`
2. Install requirements.
`pip install -r requirements.txt`
3. Run benchmark; Use index as you want for the fibonacci series.
`bash benchmark.sh 20`

## Sample Output
```
-------------------------
fibonacci_plain_recursive
-------------------------
Result: 10946
Elapsed: 4255.41 msec
Allocated: 11.90 MiB

-------------------
fibonacci_iterative
-------------------
Result: 10946
Elapsed: 0.55 msec
Allocated: 0.80 MiB

------------------------
fibonacci_tail_recursive
------------------------
Result: 10946
Elapsed: 4.63 msec
Allocated: 0.80 MiB
```


## Reference
* Chris, P. (2017, July 26). _Tail Recursion in Python_ [[Link]](https://chrispenner.ca/posts/python-tail-recursion)


