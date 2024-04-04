n = int(input())
tree = {}
for _ in range(n):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]


# 코멘트
# 입력 형식을 찾아봄

def preorder(a):
    if a == '.':
        return
    print(a, end='')
    preorder(tree[a][0])
    preorder(tree[a][1])


def inorder(a):
    if a == '.':
        return
    inorder(tree[a][0])
    print(a, end='')
    inorder(tree[a][1])


def postorder(a):
    if a == '.':
        return
    postorder(tree[a][0])
    postorder(tree[a][1])
    print(a, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
