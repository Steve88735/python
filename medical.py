medical_cause=input("do you have any medical cause")
attend= int(input("Enter the number of classes you attended"))
if medical_cause == 'Y':
    print("You are eligible for the exam")
else:
    if attend>=50:
        print("You are eligible for the exam")
    else:
        print("you are eligible for the exam")