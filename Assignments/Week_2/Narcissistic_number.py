'''
Số tự mãn (Narcissistic Number) là một số mà có tổng của từng chữ số mũ n (n >= 2) bằng chính nó.

Ví dụ:

    Số tự mãn 3 chữ số: 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3).
    Số tự mãn 4 chữ số: 8208 = (8 * 8 * 8 * 8) + (2 * 2 * 2 * 2) + (0 * 0 * 0 * 0) + (8 * 8 * 8 * 8) 

Hãy viết 1 chương trình kiểm tra xem đây có phải là số tự mãn hay không.
'''

def narcissistic(n):
    num = [int(i) for i in str(n)]
    sum = 0
    for i in num:
        sum += pow(i,len(num))
    return sum == n