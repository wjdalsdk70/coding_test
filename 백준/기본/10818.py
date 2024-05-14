# from heapq import heappush, heappop
N = int(input())
data = list(map(int, input().split()))
# max_heap = []
# min_heap = []
# # print(min(data), max(data))
# for i in data:
#     heappush(max_heap, -i)
#     heappush(min_heap, i)

# print(heappop(min_heap), -heappop(max_heap))
data.sort()
print(data[0], data[-1])
