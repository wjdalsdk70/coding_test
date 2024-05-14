from itertools import combinations
N, K = map(int, input().split())
essential_chars = {'a', 'c', 'i', 'n', 't'}
alphabet = [chr(ord('a') + i)
            for i in range(26) if chr(ord('a') + i) not in essential_chars]

words = [set(input().strip()) for _ in range(N)]

if K < 5:
    print(0)
else:
    max_count = 0
    for extra_chars in combinations(alphabet, K - 5):
        current_teachable = essential_chars.union(extra_chars)
        count = sum(1 for word in words if word.issubset(current_teachable))
        max_count = max(max_count, count)

    print(max_count)
