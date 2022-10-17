string_1 = "xâu đầu tiên "
string_2 = "xâu thứ hai"

print(string_1 + string_2)
print(string_1 * 3)
print('1' in string_1)
print('2' not in string_1)

print(ord('ω')) # char to UNICODE number
print(chr(69)) # UNICODE number to char

print(string_1[-2])
print(string_1[::-1])

# f string
f_string = f"The first string is {string_1} and the second string is {string_2}"
print(f_string)

try: 
    string_1[-1] = "4"
except Exception as e:
    print(e)

#Các hàm với string 

print(string_1.capitalize())
print(string_1.capitalize().lower())
print(string_1.title())
print(string_1.upper())
print(string_1.count('u'))

print(string_1.find("xâu"))
print(string_1.index("xâu"))
print(string_2.startswith("xâu"))
print(string_2.endswith('hai'))