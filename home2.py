work_experience = int(input("Enter your experience:"))
if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
    print("You are Middle")
elif work_experience <= 1:
    developer_type = "Junior"
    print("You are Junior")
else:
    developer_type = "Senior"  
    print("You are Senior")          