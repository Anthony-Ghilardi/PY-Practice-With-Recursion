# FUNCTION 1

# def name_args(**lots_of_args):
#     for i in lots_of_args.items():
#         print(i)
#     return

# name_args(food="Pie", verb="is", adjective="delicious")



#-------------------------------------------------------------------------------------------------------



# FUNCTION 2

# def all_true(myList):
#     return all(myList)

# print(all_true([True, True, True]))
# print(all_true([True, False]))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 3

# def maybe_true(myList):
#     return any(myList)

# print(maybe_true([True, True, True]))
# print(maybe_true([False, False]))
# print(maybe_true([True, False, False]))
# print(maybe_true([True, False, True]))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 4

# def factorial(num):
#   if num <= 1:
#     return 1
#   else:
#     return num * factorial(num-1)

# print(factorial(9))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 5 

# def recursive_deduplicate(my_str,i=0):
#   if len(my_str) <= 1 or i == len(my_str)-1:
#     return my_str
#   else:
#     if my_str[i] == my_str[i+1]:
#       return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
#     else:
#       return recursive_deduplicate(my_str,i+1)
      
# print(recursive_deduplicate("aaaa"))
# print(recursive_deduplicate("aaba"))
# print(recursive_deduplicate("apple"))
# print(recursive_deduplicate(""))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 6

# def recursive_reverse(str, i=0):
#   if len(str)==0:
#     return ""
#   #base case
#   elif i == len(str)-1:
#     return str[0]
#   else:
#     #recursive case
#     return str[-1-i] + recursive_reverse(str, i+1)

# print(recursive_reverse("aaaa"))
# print(recursive_reverse("aaba"))
# print(recursive_reverse("apple"))
# print(recursive_reverse(""))