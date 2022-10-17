# x = set(<iter>)

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x) #{'qux', 'foo', 'bar', 'baz'}

y = set("moon")
print(y)

print(set({"moon"}))

print(set([1,3,4,1,5]))

print(bool(set()))

z = {42, 'foo', 3.14159, None}

#z = {[1,2,3], [1,2,4]} 
#bug

a = {1, 3, 5, 7, 9, 11}
b = {2, 4, 6, 8, 10, 11}

print(a.union(b))
# a | b

print(a.intersection(b))
# a & b

print(a.difference(b))
# a - b

print(a.symmetric_difference(b))
# a ^ b

print(a.isdisjoint(b))

print(a.isdisjoint(b - a))

print(a.issubset(b)) # a <= b

print(a.issuperset(b)) # a>= b

a.update(b)
# a|= b

a.intersection_update(b)
# a &= b

a.difference_update(b)

a.symmetric_difference_update(b)

a.add(13)
a.pop()
a.remove(13)
a.discard(13) 
# discard: không làm gì nếu như mà ko tìm thấy phần tử yêu cầu
# remvoe: raise exception