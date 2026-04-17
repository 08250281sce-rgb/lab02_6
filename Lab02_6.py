print()
names_dict = {} 
std_id1 = (67)
std_id2 = (81)
unique_value = (std_id1 + std_id2)%10

while True:
    name = input("Enter a name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    if name in names_dict:
        print(f"{name} already exists in the dictionary.")
    else:
        names_dict[name] = unique_value
        print(f"{name} added to the dictionary with value {unique_value}.")
print()
print("Final dictionary: ", names_dict)
print()
print("Quiz Time!")
print()
