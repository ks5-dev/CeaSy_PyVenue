'''
https://projecteuler.net/problem=6

Cho dãy số tự nhiên liên tiếp từ 1 đến 100. Tính hiệu của bình phương tổng các số và tổng bình phương các số 
'''

def find_difference():
    #sum of the square
    a = int(input())
    b = int(input())
    sum_square = 0
    for i in range(a,b+1):
        sum_square += i*i
    #square of the sum
    square_sum = 0
    for i in range(a,b+1):
        square_sum += i
    square_sum = square_sum * square_sum

    return square_sum - sum_square

print(find_difference())
