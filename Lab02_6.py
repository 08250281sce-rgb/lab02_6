std1_id=input("enter student id:")
std2_id=input("enter student id:")
#last two digit std no:
last_two_1=int(std1_id[-2:])
last_two_2=int(std2_id[-2:])
print(last_two_1)
print(last_two_2)
#add the last number and divide it by 10 
unique_value=(last_two_1+last_two_2)%10
print(f"The unique value = {unique_value}")
