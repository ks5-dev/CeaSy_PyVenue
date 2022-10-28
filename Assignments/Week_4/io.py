import os

'''
Trong thư mục stories có 1 file bị là "little_match_girl.txt" (cô bé bán diêm đấy) file đó bị lỗi về format nên ta muốn là sửa lại
1) Sử dụng os.path.join() để lấy được đường dẫn của file kia lưu trong 1 biến, tương tự làm thế để lưu 1 biến khác có đường dẫn như vậy nhưng mà tệp là 
"little_match_girl_modified.txt" và file này chưa được tạo.
File đấy sẽ dùng là bản đã được sửa của file.txt ban đầu, ta tiến hành sửa như sau: 
- Lỗi format của file ban đầu là sau mỗi một dòng thì nó bị cách dòng, hãy loại bỏ cách dòng này
- Sau đó thì thêm tiêu đề là "Little Match Girl" vào đầu file mới.
- Viết ra tệp nội dung đã được chỉnh sửa
'''

file = os.path.join(os.getcwd(), "short_stories/little_match_girl.txt")
file_2 = os.path.join(os.getcwd(), "short_stories/little_match_girl_modified.txt")

with open(file, "r") as r:
    content = r.readlines()
    r.close()

for i in content:
    if i == "\n":
        content.remove(i)

content.insert(0, "Little Match Girl")

with open(file_2, "w+") as r:
    r.writelines(content)
   