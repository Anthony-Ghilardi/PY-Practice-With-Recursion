# FUNCTION 1

# def max_num(*numberList):
#     if len(numberList) == 3:
#         print(max(numberList))
#     else:
#         print("List can only have three numbers")

# max_num(10, 15, 100)
# max_num(10, 15)



#-------------------------------------------------------------------------------------------------------



# FUNCTION 2

# def mult_list(number_list):
#     result = 1
#     for i in number_list:
#         result = result * i
#     return(result)

# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(mult_list(list1))
# print(mult_list(list2))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 3
# def rev_string(x):
#     return x[::-1]

# reversedString = rev_string("Wow who knew python was so cool")

# print(reversedString)



#-------------------------------------------------------------------------------------------------------



# FUNCTION 4
# def num_within(num, start, end):
#     if num >= start and num <= end:
#         return True
#     else:
#         return False
    
# num = 2 # Change this number to test the function
# start = 1
# end = 10

# print(num_within(num, start, end))



#-------------------------------------------------------------------------------------------------------



# FUNCTION 5 
# triangle = [[1],[1,1]]
# def pascal(n):
#   if n < 1:
#     print("invalid number of rows")
#   elif n == 1:
#     print(triangle[0])
#   else:
#     row_number = 2
#     while len(triangle) < n:
#       row = []
#       row_prev = triangle[row_number - 1]
#       length = len(row_prev)+1
#       for i in range(length):
#         if i == 0:
#           row.append(1)
#         elif i > 0 and i < length-1:
#           row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
#         else:
#           row.append(1)
#       triangle.append(row)
#       row_number += 1

#     for row in triangle:
#       print(row)

# pascal(2)
# pascal(5)