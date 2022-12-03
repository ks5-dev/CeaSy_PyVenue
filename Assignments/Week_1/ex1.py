'''
Bài 1
Viết một hàm với 3 tham số, hàm này sẽ in ra kiểm tra 3 đối số phải là số nguyên không với lệnh isdigit(), nếu có thì in nó ra và nếu không thì in “Not a digit"

'''

def func(arg1, arg2, arg3):
    if arg1.isdigit():
        print(arg1)
    else:
        print("Not a digit")
    if arg2.isdigit():
        print(arg2)
    else:
        print("Not a digit")
    if arg3.isdigit():
        print(arg3)
    else:
        print("Not a digit")

def func(arg1, arg2, arg3):
    arg_list  =[arg1, arg2, arg3]
    for i in arg_list:
        if i.isdigit():
            print(i)
        else:
            print("Not a digit")
func("12", "No", "45")