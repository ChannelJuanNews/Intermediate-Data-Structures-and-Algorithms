def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    array = [None] * n
    array[0] = 0
    array[1] = 1

    if n > 2:
        for i in range(2,n):
            array[i] = array[i-1] + array[i-2]
        return array[n - 1]

print(fib2(100))
