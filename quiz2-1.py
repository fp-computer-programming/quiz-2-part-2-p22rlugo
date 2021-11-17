# Ryan Lugo: RJL 11/17/21

class_meet = input("What cycle day do you want to see if you meet on? (A - G): ")

if class_meet.lower() == "a":
    print(str.format("You have class today because it is A day."))
elif class_meet.lower() == "b":
    print(str.format("You don't have class today because it is B day."))
elif class_meet.lower() == "c":
    print(str.format("You have class today because it is C day."))
elif class_meet.lower() == "d":
    print(str.format("You don't have class today because it is D day."))
elif class_meet.lower() == "e":
    print(str.format("You have class today because it is E day."))
elif class_meet.lower() == "f":
    print(str.format("You don't have class today because it is F day."))
elif class_meet.lower() == "g":
    print(str.format("You don't have class today because it is G day."))
elif class_meet == "":
    print(str.format("You did not input a cycle day! Remember (A - G)"))
else:
    print(str.format("You did not input a correct cycle class letter! Remember (A - G)"))