# Cho một danh sách
# Tìm nguyên tố mà số lần xuất hiện của nó là lẻ


def find_it(seq):
    for i in range(len(seq)):
        count = 0
        for j in range(len(seq)):
            if seq[i] == seq[j]:
                count+=1

        if (count % 2 != 0):
            return seq[i]