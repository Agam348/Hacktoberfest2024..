# initializing list
test_list = ["1-2", "3-4-8-9", "4-10-4"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = "-"
 
# conversion using split and list comprehension
# int() is used for conversion
res = [tuple(int(ele) for ele in sub.split(K)) for sub in test_list]
 
# printing result
print("The converted tuple list : " + str(res))
