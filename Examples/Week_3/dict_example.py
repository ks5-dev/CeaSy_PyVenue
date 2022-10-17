a = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
# key - value
b = {'a': 0 , 'b':1, int:4}

print(b['a'])
print(b[int])

c = {"list_1": [0, 1], "list_2": [2, 3]}
print(c["list_2"][0])

c["list_3"] = [4, 5]
print(c)

#d = {"list_1": [0, 1], "list_1": [0, 1]}   # bug vì có key lặp lại

c["list_1"] = [3,5]

# e = {[1,2]: [1,2]} # bug vì có key có thể biến đổi (mutable)

'''
Giới hạn của từ điển:
    - Key ko bị lặp
    - Key phải là đối tượng mà ko thể bị đổi (immutable)
Không có giới hạn lên value
'''

len(c)


print(c.get("list_3"))
c.items()
c.keys()
c.values()
print(c.pop("list_3")) # Xóa list_3 và trả về cặp giá trị mà list_3 đang giữ  
c.popitem()
c.clear()

a.update(b) # Bây giờ a có thêm tất cả các phần tử của b