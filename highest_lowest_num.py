#highest number in the list
l = [6,56,5,9,22]
n = 0
for i in range(len(l)):
    if l[i] > n:
        n =l[i]
print(n)

#lowest num in the list
l = [3,6,56,5,9,22]
n = l[0]
for i in range(len(l)):
    if l[i] <n:
        n = l[i]
print(n)