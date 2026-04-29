print()
student1_id = input("Enter Student 1 ID: ") # Asking for student IDs
student2_id = input("Enter Student 2 ID: ") 

# Getting the last two digits from each ID
last_two_1 = int(student1_id[-2:])
last_two_2 = int(student2_id[-2:])

# Generating unique value
unique_value = (last_two_1 + last_two_2) % 10
print() 
student = {}

while True: # Loop to input student names
    name = input("Enter student name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break
    if name == "":
        print("WARNING! No name is entered. Skipping...\n")
        continue
    student[name] = 0 # Initialize score to 0 for each student
print("\nStudent names in the system: ")
for name in student:
    print("-", name)
print("\n----- Quiz Time! -----\n")
for name in student:
    print(f"\nQuiz for {name}: ")
    score = 0

    ans1 = int(input(f"Question 1: {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1
    ans2 = int(input(f"Question 2: {unique_value} * 3 = "))
    if ans2 == unique_value * 3:
        score += 1
    ans3 = int(input(f"Question 3: {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1
    
    student[name] = score
    # Determine performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Needs Improvement"
    else:
        performance = "Poor"
    
    if score == 0:
        print("WARNING! Your score is 0.")
    # Determine certificate eligibility
    if score >= 2: 
        certificate = "Eligible for Certificate."
    else:
        certificate = "Not eligible for Certificate."
    print(f'Score: {score}')
    print(f'Performance: {performance}')
    print(f'Certificate Status: {certificate}')
# Displaying results
    if score==3:
       for i in range(1, score + 1):
        print("✳️  " * i)
    if score==2:
       for i in range(1, score + 1):
        print("✳️  " * i)
    if score==1:
       for i in range(1, score + 1):
        print("✳️  " * i)
print("\n----- Quiz Ended -----")
print()
