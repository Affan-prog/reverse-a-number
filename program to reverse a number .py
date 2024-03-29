

num = int(input("Enter number :"))

# str_num = str(num)
# len_num = len(str_num)


# 1st method i.e By Converting number into string

# reversed_number = str_num[::-1]

# print("Reversed number :",reversed_number)



# Using for loop ( not the best way to do it)
# 2nd method i.e Using list , then iterating it

# =====================================

# lst = []

# for i in range(1,len_num+1):
#     last_digit = num%10
#     lst.append(last_digit)
    
#     new_num = num//10
#     num = new_num

# for reversed_num in lst:
#     print(reversed_num, end='')

# =====================================

# 3rd method : using while loop (best way to do it)

reverse = 0

while(num!=0):

    last = num%10
    num = num//10
    reverse = (reverse*10)+last

print(reverse)









