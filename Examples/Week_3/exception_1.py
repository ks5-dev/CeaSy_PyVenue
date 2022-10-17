# Giới thiệu về excpetion khi mà ta xác định được cụ thể một lỗi mà code dễ mắc phải

def spam(divideBy):
    return 42 / divideBy

# ZeroDivision
'''
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
finally:
    print('This print statement is always executed')
'''
# FileNotFound
'''
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    raise FileNotFoundError 
'''

'''
https://pythonguides.com/python-exceptions-handling/
NameError
ImportError
TypeError
...
'''

try: 
    import lmao
except ImportError:
    raise ImportError
