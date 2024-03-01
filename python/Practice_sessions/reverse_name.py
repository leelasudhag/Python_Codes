#given a name (firstname lastname) reverse the name(lastname firstname)
"""name  = "sriram leela kondapalli"
my_list = (name.split(" "))
print(x)

for y in x:
    print(y)
    """

# #my_list = [1, 2, 3, 4, 5,9,15]
# name  = "sriram leela kondapalli gadde vetlapalem"
# my_list = (name.split(" "))
# print(my_list)
# new_list = []
# for i in range(len(my_list)):
#     new_list.insert(i,my_list[-1])
#     my_list.pop(-1)
# print(" ".join(new_list))
from bitarray.util import strip

name  = "sriram, kondapalli"

output  = "kondapalli, sriram"

my_list = (name.split(","))
print(my_list)
new_list = []
for i in range(len(my_list)):
    new_list.insert(i,(my_list[-1]).strip())
    my_list.pop(-1)
print(", ".join(new_list))