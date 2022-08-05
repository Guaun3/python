def grade_level():
    grade = int(
        input("what grade did you get: \n(the input must be between 0-100)"))
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 60 <= grade <= 79:
        return "C"
    elif 40 <= grade <= 59:
        return "D"
    elif 0 <= grade <= 39:
        return "E"
    else:
        return "invalid number"


def print_odd_even():
    for i in range(100):
        if i % 2 == 0:
            print(f"{i} is even")


'''
L2-202
continue: skip one time
break: end this loop
'''


def print_room():
    # floor level
    for i in range(1, 6):
        print(f"---------level {i}---------")
        if i == 3:
            continue
        # room number
        for j in range(1, 9):
            if i == 4 and j == 4:
                print("haunted house....run!")
                break
            print(f"room L{i}-{i}0{j}")


def print_triangle():
    for i in range(10):
        if i <= 5:
            print("*"*i)
        else:
            print("*"*(10-i))


def dead_loop():
    count = 0
    while True:
        count +=1
        print(f"{count}th loop")
        

def multiplication_table():
    for i in range (1, 10):
        for j in range (1, i+1):
            print(f"{i}*{j}={i*j}", end=" ")
        print()


if __name__ == "__main__":
    # print(grade_level())
    # print_odd_even()
    # print_room()
    # print_triangle()
    multiplication_table()

    
    