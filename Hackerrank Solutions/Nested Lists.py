if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        
arr.sort(key= lambda x: x[1])
result = []

for i in arr:
    if arr[0][1] != i[1]:
        second_lowest = i
        break
        
for i in arr: 
    if i[1] == second_lowest[1]:
        result.append(i)
result.sort()
for x in result:
    print(x[0])
