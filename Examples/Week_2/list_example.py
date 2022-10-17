# Giới thiệu về danh sách
list_a = [1, 34, 23, 67, 89, 101, 203, 46]

list_b= ["string", 1, True, 2.3, [1,2], 7+8j]

# list_indice

print(list_a[2])
print(list_b[1:3])
print(list_a[1:7:2])
print(list_a[-1])
print(list_a[::-1])

print(len(list_b))
print(min(list_a))
print(max(list_a))

# mảng

nested = [ [1, 2, 4],
        [2, 5, 6],
        [9, 9, 0] ]
print(nested[0][1])


list_a[0] = 12
list_a[2:4] = [24,12,15]
print(list_a)

list_a += [12]
list_a.append(12)
list_a.extend([12,13])

list_a.insert(2, 111111)

list_a.remove(3)

list_a.pop()

#list comprehension 

x = [i for i in range(0,12)]
y = [i for i in range(0,12) if x%2==0]