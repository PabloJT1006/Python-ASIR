

def Fibonacci():
    n = int(input("Introduce "))
    arr = []
    arr.append(0)
    arr.append(1)
    n1 = 0
    n2 = 1
    while True:
        y = arr[n1] + arr[n2]
        if y < n:
            arr.append(y)
            n1 += 1
            n2 += 1
        else:
            break
    for i in arr:
        print (i, end=" ")
    print("")
    print(arr)
        

Fibonacci()