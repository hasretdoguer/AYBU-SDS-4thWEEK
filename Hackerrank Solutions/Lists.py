if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command, *numbers = input().split()
        n_arr = list(map(int, numbers))
        
        if command == "append":
            arr.append(n_arr[0])
            continue
        if command == "insert":
            arr.insert(n_arr[0],n_arr[1])
            continue
        if command == "print":
                print(arr)
                continue
        if command == "remove":
            arr.remove(n_arr[0])
            continue
        if command == "sort":
            arr.sort()
            continue
        if command == "pop":
            arr.pop()
            continue
        if command == "reverse":
            arr.reverse()
            continue
