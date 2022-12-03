a = True
if a:
   print("Yes")
else:
   print("No")

b =14
if b%2 == 0:
   print("14 is even")
elif b%2 == 1:
   print("14 is odd")
else:
   print("Huh")

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))