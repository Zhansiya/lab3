a = []
a = [1, 2, "abc", 1.12]
b = (1, 2, "abc", 1.12)
a.append("abc")
n = len(b)
#for i in range(n, 0, -1):
#    print(i)
for i in b:
    print(i, type(i))