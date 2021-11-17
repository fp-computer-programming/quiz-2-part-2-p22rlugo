# Ryan Lugo: RJl 11/17/21

# First Set logic
first_set = str(input("Enter your first set of directions!: "))
first_split = first_set.split(" ")
first_list = list(first_split)

# Second Set Logic
second_set = str(input("Enter your second set of directions!: "))
second_split = second_set.split(" ")
second_list = list(second_split)

# North = 1 , East = 2 , South = 3 , West = 4


# Tables for given values
directions_table = [1,1,1,1,1,1] # This is a terrible way to solve the problem but under a time crunch :/
set_table = first_list,second_list

# Also this doesn't account for people putting in different words
# If logic (Be prepared for LOTS of ELIFS)
if len(first_list) > 3 or len(second_list) > 3:
    print(str.format("Your set of directions is longer than the maximum value that you can input! (3 directions)"))
else:
    # 1st Direction
    if first_list[0].lower() == "north":
        directions_table[0] = 1
    elif first_list[0].lower() == "east":
        directions_table[0] = 2
    elif first_list[0].lower() == "south":
        directions_table[0] = 3
    elif first_list[0].lower() == "west":
        directions_table[0] = 4
    # 2nd Input
    if first_list[1].lower() == "north":
        directions_table[1] = 1
    elif first_list[1].lower() == "east":
        directions_table[1] = 2
    elif first_list[1].lower() == "south":
        directions_table[1] = 3
    elif first_list[1].lower() == "west":
        directions_table[1] = 4
    # 3rd input
    if first_list[2].lower() == "north":
        directions_table[2] = 1
    elif first_list[2].lower() == "east":
        directions_table[2] = 2
    elif first_list[2].lower() == "south":
        directions_table[2] = 3
    elif first_list[2].lower() == "west":
        directions_table[2] = 4
    # 2nd Set of Directions
    if second_list[0].lower() == "north":
        directions_table[3] = 1
    elif second_list[0].lower() == "east":
        directions_table[3] = 2
    elif second_list[0].lower() == "south":
        directions_table[3] = 3
    elif second_list[0].lower() == "west":
        directions_table[3] = 4
    # 2nd Input
    if second_list[1].lower() == "north":
        directions_table[4] = 1
    elif second_list[1].lower() == "east":
        directions_table[4] = 2
    elif second_list[1].lower() == "south":
        directions_table[4] = 3
    elif second_list[1].lower() == "west":
        directions_table[4] = 4
    # 3rd Input
    if second_list[2].lower() == "north":
        directions_table[5] = 1
    elif second_list[2].lower() == "east":
        directions_table[5] = 2
    elif second_list[2].lower() == "south":
        directions_table[5] = 3
    elif second_list[2].lower() == "west":
        directions_table[5] = 4
print(str.format("In order to have the robot move"+str(set_table)+"give it this sequence"+str(directions_table)+"."))