N, K = map(int, input().split())
data = list(map(int, input().split()))
use = []
count = 0

for i in range(K):
    if len(use) < N:
        if data[i] not in use:
            use.append(data[i])
    elif data[i] in use:
        continue
    else:
        # Find the page in `use` that will not be needed for the longest time
        farthest_use_index = -1
        replace_index = -1

        for index, page in enumerate(use):
            if page not in data[i+1:]:
                replace_index = index
                break
            next_use = data[i+1:].index(page)

            if next_use > farthest_use_index:
                farthest_use_index = next_use
                replace_index = index

        # Replace the page that is not needed for the longest time
        use[replace_index] = data[i]
        count += 1

print(count)
