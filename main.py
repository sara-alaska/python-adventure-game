# Choose your own adventure
# CS 3620
# Sara Alaskarova
# Your story will be saved in the game_history.txt

# To add a pause
import time

# Figure out how users will respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Error messages
required = "\nUse only A or B \n"
required2 = "\nUse only A or B or C \n"

required_y_n = "\nUse only Y or N"

log = open("game_history.txt", 'w')


# Writes the output in the .txt file and prints it
def write_print(output):
    print(output)
    global log
    log.write(output)
    return ()


def print_choice():
    return ">>>"


# Opens the .txt files and splits the text into paragraphs
def open_file(filename):
    with open(filename, "r") as paragraph:
        read_paragraph = paragraph.read().split("\n\n")
    return read_paragraph


def intro():
    read_paragraph = open_file("intro.txt")
    write_print(read_paragraph[0])
    time.sleep(1)
    print(read_paragraph[1])
    choice = input(print_choice())  # Choice 1
    if choice in answer_A:
        option_stock_up()
    elif choice in answer_B:
        write_print(read_paragraph[2])  # ending 1
        time.sleep(1)
        restart()
    else:
        print(required)
        restart()


# restart the game
def restart():
    file = open("restart_game.txt", "r")
    data = file.read()
    print(data)
    file.close()
    restart_choice = input(print_choice())  # choice 2
    if restart_choice in yes:
        intro()
    elif restart_choice in no:
        exit(0)
    else:
        print(required_y_n)
        restart()


def option_stock_up():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[0])
    time.sleep(1)
    print(read_paragraph[1])
    choice = input(print_choice())  # choice 3
    if choice in answer_A:
        option_escape()
    elif choice in answer_B:
        option_stay_at_home()
    else:
        write_print(required)
        restart()


def option_escape():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[2])
    time.sleep(1)
    print(read_paragraph[3])
    choice = input(print_choice())  # choice 4
    if choice in answer_A:
        option_mountains()
    elif choice in answer_B:
        option_south()  # ending 2
    else:
        print(required)
        restart()


def option_mountains():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[4])
    time.sleep(1)
    print(read_paragraph[5])
    choice = input(print_choice())  # Choice 5
    if choice in answer_A:
        write_print(read_paragraph[6])  # ending 3
        restart()
    elif choice in answer_B:
        option_go_around()
    else:
        print(required)
        restart()


def option_south():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[7])  # ending 4
    restart()


def option_go_around():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[8])
    time.sleep(1)
    print(read_paragraph[9])
    choice = input(print_choice())  # choice 6
    if choice in answer_A:
        option_approach_them()
    elif choice in answer_B:
        option_go_the_other_way()
    else:
        print(required)
        restart()


def option_approach_them():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[10])
    time.sleep(1)
    print(read_paragraph[11])
    choice = input(print_choice())  # choice 6
    if choice in answer_A:
        option_join()
    elif choice in answer_B:
        option_dont_join()
    else:
        print(required)
        restart()


def option_join():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[12])
    write_print("\n The end!")
    restart()


def option_dont_join():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[13])
    restart()


def option_go_the_other_way():
    option_dont_join()


def option_stay_at_home():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[14])
    time.sleep(1)
    print(read_paragraph[15])
    choice = input(print_choice())  # choice 7
    if choice in answer_A:  # ending 4
        write_print(read_paragraph[16])
        restart()
    elif choice in answer_B:
        option_offer_cherries()
    elif choice in answer_C:
        option_out_of_here()
    else:
        print(required2)
        restart()


def option_out_of_here():
    option_escape()


def option_offer_cherries():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[18])
    time.sleep(1)
    print(read_paragraph[19])
    choice = input(print_choice())  # choice 8
    if choice in answer_A:
        option_offer_tea()
    elif choice in answer_B:
        option_offer_cofee()
    else:
        print(required)
        restart()


def option_offer_cofee():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[20])
    time.sleep(1)
    print(read_paragraph[21])
    choice = input(print_choice())  # choice 9
    if choice in answer_A:
        option_wait_cofee()
    elif choice in answer_B:
        option_give_sandwich()
    else:
        print(required)
        restart()


def option_wait_cofee():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[22])
    restart()  # ending 5


def option_give_sandwich():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[23])
    restart()  # ending 6


def option_offer_tea():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[26])
    time.sleep(1)
    print(read_paragraph[27])
    choice = input(print_choice())  # choice 10
    if choice in answer_A:
        option_be_friends()
    elif choice in answer_B:
        option_tea_trade()
    else:
        print(required)
        restart()


def option_be_friends():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[28])
    restart()


def option_tea_trade():
    read_paragraph = open_file("options.txt")
    write_print(read_paragraph[29])
    write_print("\nThe end!")  # ending 6


intro()

log.close()
