'''
Tìm số nhỏ thứ n trong một danh sách

Vd : số nhỏ thứ 3 trong danh sách [4, 7, 8, 2, 12, 15] 
Output là 7 vì 2 < 4 < 7 < 8 < 12 < 15

Gợi ý là bài này nên dùng sort
'''
def find_n(arr,i):
    return sorted(arr)[i-1]

print(find_n([4, 7, 8, 2, 12, 15], 3))