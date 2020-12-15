
import random

squares = {
"1.1" : 0, "1.2" : 0, "1.3" : 0, "1.4" : 0,
"2.1" : 0, "2.2" : 0, "2.3" : 0, "2.4" : 0,
"3.1" : 0, "3.2" : 0, "3.3" : 0, "3.4" : 0,
"4.1" : 0, "4.2" : 0, "4.3" : 0, "4.4" : 0,
}

printed_squares = {
"1.1" : "____", "1.2" : "____", "1.3" : "____", "1.4" : "____",
"2.1" : "____", "2.2" : "____", "2.3" : "____", "2.4" : "____",
"3.1" : "____", "3.2" : "____", "3.3" : "____", "3.4" : "____",
"4.1" : "____", "4.2" : "____", "4.3" : "____", "4.4" : "____",
}


def print_board(squares):
    print(printed_squares["1.4"] + "  |  " + printed_squares["2.4"] + "  |  " + printed_squares["3.4"] + "  |  " + printed_squares["4.4"] + "  |  ")
    print(printed_squares["1.3"] + "  |  " + printed_squares["2.3"] + "  |  " + printed_squares["3.3"] + "  |  " + printed_squares["4.3"] + "  |  ")
    print(printed_squares["1.2"] + "  |  " + printed_squares["2.2"] + "  |  " + printed_squares["3.2"] + "  |  " + printed_squares["4.2"] + "  |  ")
    print(printed_squares["1.1"] + "  |  " + printed_squares["2.1"] + "  |  " + printed_squares["3.1"] + "  |  " + printed_squares["4.1"] + "  |  ")
    print("________")
    print("________")

def update_square(square, value): #takes square str key and int value
    squares[square] = value
    update_printed_square(square, value)


def update_printed_square(square, value): #takes square str key and int value
    if value == 0:
        printed_squares[square] = "____"
    if len(str(value)) == 1 and squares[square] != 0:
        printed_squares[square] = "_0{value}_".format(value=value)
    elif len(str(value)) == 2:
        printed_squares[square] = "_{value}_".format(value=value)
    elif len(str(value)) == 3:
        printed_squares[square] = "0{value}".format(value=value)
    elif len(str(value)) == 4:
        printed_squares[square] = "{value}".format(value=value)

def condense_squares(s1, s2):
    if squares[s2] == 0:
        update_square(s2, squares[s1])
        update_square(s1, 0)
    elif squares[s1] == squares[s2]:
        update_square(s2, (squares[s1] + squares[s2]))
        update_square(s1, 0)


def move_up():
    for x in range(1,5):
        for y in range(1,4):
            square = "{x}.{y}".format(x=x, y=4-y)
            upper_neighbor = square[0] + square[1] + str((int(square[2]) + 1))
            while int(upper_neighbor[2]) < 5:
                condense_squares(square, upper_neighbor)
                square = upper_neighbor
                upper_neighbor = square[0] + square[1] + str((int(square[2]) + 1))
    generate_new_placement()
    print_board(squares)

def move_down():
    for x in range(1, 5):
        for y in range(2, 5):
            square = "{x}.{y}".format(x=x, y=y)
            lower_neighbor = square[0] + square[1] + str((int(square[2]) - 1))
            while int(lower_neighbor[2]) > 0:
                condense_squares(square, lower_neighbor)
                square = lower_neighbor
                lower_neighbor = square[0] + square[1] + str((int(square[2]) - 1))
    generate_new_placement()
    print_board(squares)

def move_right():
    for x in range(1, 4):
        for y in range(1, 5):
            square = "{x}.{y}".format(x=4-x, y=y)
            right_neighbor = str((int(square[0]) + 1))  + square[1] + square[2]
            while int(right_neighbor[0]) < 5:
                condense_squares(square, right_neighbor)
                square = right_neighbor
                right_neighbor = str((int(square[0]) + 1)) + square[1] + square[2]
    generate_new_placement()
    print_board(squares)

def move_left():
    for x in range(2, 5):
        for y in range(1, 5):
            square = "{x}.{y}".format(x=x, y=y)
            left_neighbor = str((int(square[0]) - 1)) + square[1] + square[2]
            while int(left_neighbor[0]) > 0:
                condense_squares(square, left_neighbor)
                square = left_neighbor
                left_neighbor = str((int(square[0]) - 1)) + square[1] + square[2]
    generate_new_placement()
    print_board(squares)

def generate_new_placement():
    squares_with_zero = [square for square in squares if squares[square] == 0]
    square = random.choice(squares_with_zero)
    num = random.choice([2,4])
    update_square(square, num)


def get_move():
    move = input("What's your move? Enter 1 for Up, 2 for Down, 3 for Left, 4 for Right, or q to quit:  ")
    if move == "1":
        move_up()
    elif move == "2":
        move_down()
    elif move == "3":
        move_left()
    elif move == "4":
        move_right()
    elif move == "q":
      print("quitting the game...")
      return "q"
    else:
        print("Invalid move.")



update_square("1.1", 2)
update_square("1.2", 2)

update_square("3.1", 2)
update_square("3.2", 2)
update_square("3.3", 2)
update_square("3.4", 4)


print("Welcome to the 2048 game terminal app. To play, enter 1, 2, 3, or 4 to move all values up, down, left, or right (respectively). The squares will sum and condense if two values are equal, and a new value of 2 or 4 will appear on the board. To win, create a square with the value 2048. We'll seed a few values to get you started. Good luck!")
print_board(squares)

for i in range(100):
    if get_move() == 'q': break
    if 2048 in squares.values():
        print("Congratulations! You've won the game")
        break
    elif i == 99 : 
        print("You've tried way too many times and still haven't won...Too bad!")
