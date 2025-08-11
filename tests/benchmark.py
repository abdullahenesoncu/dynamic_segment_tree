import time
import random
from dynamic_segment_tree import DynamicSegTree

def test_benchmark_dynamic_segment_tree():
    N = 10_000_000
    M = 1000
    Q = 100_000  # reduced for quicker test runs; change as needed

    st = DynamicSegTree(N)

    # Random updates
    start = time.time()
    for _ in range(Q):
        idx = random.randint(0, N-1)
        cat = random.randint(0, M-1)
        val = random.randint(1, 10)
        st.update(idx, cat, val)
    end = time.time()
    print(f"Updates: {Q} in {end-start:.2f}s")

    # Random queries
    start = time.time()
    for _ in range(Q):
        l = random.randint(0, N-1)
        r = random.randint(l, min(N-1, l+1000))
        cat = random.randint(0, M-1)
        _ = st.query(l, r, cat)
    end = time.time()
    print(f"Queries: {Q} in {end-start:.2f}s")
