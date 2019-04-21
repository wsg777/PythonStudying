# 选择排序
A = [11, 39, 38, 55, 86, 5, 37, 12, 4, 11, 18]
print('原列表：' + str(A))
for i in range(len(A)):
    j = i
    while j < len(A):
        if A[i] > A[j]:
            t = A[i]
            A[i] = A[j]
            A[j] = t
        j += 1
print('选择排序：' + str(A))

# 冒泡排序
A = [11, 39, 38, 55, 86, 5, 37, 12, 4, 11, 18]
for i in range(len(A)):
    j = len(A) -1
    while j > i:
        if A[j-1] > A[j]:
            t = A[j-1]
            A[j-1] = A[j]
            A[j] = t
        j -= 1
print('冒泡排序：' + str(A))

# 插入排序
A = [11, 39, 38, 55, 86, 5, 37, 12, 4, 11, 18]
for i in range(len(A)-1):
    j = i + 1
    t = A[j]
    while j > 0 and t < A[j-1]:
        A[j] = A[j-1]
        j -= 1
    A[j] = t
    i += 1
print('插入排序：' + str(A))

# 并归排序
A = [11, 39, 38, 55, 86, 5, 37, 12, 4, 11, 18]
def merge(a):
    l = len(a)
    if l % 2 == 0:
        l1 = l/2
        l2 = l/2
    else:
        l1 = (l+1)/2
        l2 = (l-1)/2
    a1 = []
    a2 = []
    for i in l1:
        a1.append(a[i])
    for i in l2:
        a2.append(a[i+l1])

    if len(a1) > 1:
        merge(a1)
    if len(a2) > 1:
        merge(a2)








