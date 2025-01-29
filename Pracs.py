with open('praks') as file:
    a = file.readlines()
    b = a[0].split()
    sort = sorted(a, key=lambda x: x[13:15])
print(sort)
# a = [8,9,4,15,1,3]
# a = sorted(a)
# print(a)2
