# Tail Recursion in Python


## Installation
1. Clone repository
`git@github.com:waegaein/tail-recursion.git`
2. Install requirements
`pip install -r requirements.txt`
3. Run benchmark
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
