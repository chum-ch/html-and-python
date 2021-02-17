

array = [0,1,0,0,0,0,0]
action = input("Enter the action: ")
index_of_one = 0
if array[0] == 1 and action.upper() == "L":
    print("We cannot move!")
elif array[-1] == 1 and action.upper() == "R":
    print("We cannot move!")
else:
    count_right = 0
    count_left = 0
    for index_array in range(len(array)):
        if array[index_array]:
            index_of_one = index_array
    for character in action:
        if character.upper() == "R":
            count_right += 1
            array[index_of_one + count_right] = 1
            array[index_of_one] = 0
        elif character.upper() == "L":
            count_left -= 1
            array[index_of_one - count_left] = 1
            array[index_of_one] = 0
    print(array)