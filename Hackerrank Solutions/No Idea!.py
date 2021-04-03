hapiness = 0
n, m = map(int, input().strip().split(' '))
arr = map(int, input().strip().split(' '))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
    
for i in arr:
    if i in A:
        hapiness += 1
    elif i in B:
        hapiness -= 1
        
print(hapiness)
