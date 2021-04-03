if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
arr = []
for i in range(x+1):
    for k in range(y+1):
        for t in range(z+1):
            if not i+k+t == n:
                arr.append([i,k,t])
print(arr)


