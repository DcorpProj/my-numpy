from myarray import *
my_array = MyArray(2, 3, 10, 2)
print(my_array)  # [[10, 12, 14], [10, 12, 14]]
my_array[0][0] = 20
print(my_array)  # [[20, 12, 14], [10, 12, 14]]
