def check_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**1/2)+1):
        if n % i == 0:
            return False
    return True

for i in range(1,21):
    if check_prime(i):
        print(str(i) + " is a prime number")
    else:
        print(str(i) + " is not a prime number")

def get_prime(input_list):
    for i in input_list:
        if not check_prime(i):
            input_list.remove(i)
    return input_list

print(get_prime([23, 45, 67]))