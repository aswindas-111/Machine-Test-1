def squares(n):
    numbers = {}
    for i in range(1,n+1):
        numbers[i] = i*i
    print(numbers)


squares(5)