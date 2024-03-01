name = "youtube"
print(name)
print(name[0])
print(name[-2])
myname = "leela"
print(len(myname))
print('sudha' + myname)
# lists [] - mutable
nums = [25, 12, 36, 94]
print(nums)
print(nums[2])
print(nums[:2])
names = ['leela', 'sasi', 'sriram']
print(names)
result = [nums, names]
print(result)
nums.insert(0, 5)
print(nums)
nums.remove(36)
print(nums)
print(min(nums))
print(sum(nums))
nums.sort()
print(nums)
# tuples () - immutable
tup = (10, 28, 40, 89)
print(tup)
print(tup[1])
# set {}
s = {24, 56, 67, 98,}
print(s)
# variables
num = 5
print(id(num))
PI = 3.14
print(PI)
PI = 3.15
print(PI)
print(type(PI))
# conversion from string to int  vice versa
a = 5.6
b = int(a)
c = float(a)
d = 6 + 8j
print(b, c)
print(type(b))
print(type(c))
print(type(d))
b = complex(d)
print(b)
range(0, 10)
print(list(range(2,10, 1)))
# dictionary {}
d = {'sasi' : 'iphone14', 'sudha' : 'iphone15', 'sriram' : 'samsung'}
print(d.keys())
print(d.values())
print(d.keys(), d.values())
print(bin(21))
print(0b10101)
 #x = int(input("enter the 1st number"))
# y = int(input("enter the 2nd number"))
# z = x + y
#print(z)

if False:
    print("this statement")
else:
    print("bye")

x =0
while x <=5:
    print(x)
    x=x+1

i = 10
while i >1:
    print(i)
    i=i-1

x=0
while x<=5:
    print("sudha is practicing python")
    x=x+1