def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

# 1 1 2 3 5 8 13 ...

def list_fibonacci(n):
    list_of_fibonacci = []
    for i in range(0,n+1):
        list_of_fibonacci.append(fibonacci(i))
    return list_of_fibonacci
    # Nếu như muốn loại số 0
    # return list_of_fibonacci[1:] 
    
m = int(input())
print(list_fibonacci(m))