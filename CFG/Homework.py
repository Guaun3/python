import math
"""
Session 1
"""


def S1Q1():
    """
    Question 1:
    I am building some very high quality chairs and need exactly four nails for each chair. I've written a program to calculate how many nails I need to buy to build these chairs.
    chairs = '15'
    nails = 4 s
    total_nails = chairs * nails
    message = 'I need to buy {} nails'.format(total_nails)
    print('You need to buy {} nails'.format(message))

    When I run the program it tells me that I need to buy 15151515 nails.
    This seems like a lot of nails.
    Is my program calculating the total number of nails correctly?
    What is the problem? How do I fix it?
    """
    chairs = '15'
    nails = 4
    total_nails = int(chairs) * nails
    message = "I need to buy {} nails".format(total_nails)
    print(message)


def S1Q2():
    """
    Question 2
    I'm trying to run this program, but I get an error.
    What is the error telling me is wrong? How do I fix the program?
    my_name = Penelope
    my_age = 29
    message = 'My name is {} and I am {} years old'.format(my_name, my_age)
    print(message)
    """
    # Ans: NameError: name 'Penelope' is not defined, Penelope is string and need "" around it
    my_name = "Penelope"
    my_age = 29
    message = 'My name is {} and I am {} years old'.format(my_name, my_age)
    print(message)


def S1Q3():
    """
    Question 3
    I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
    Write a program to calculate this.
    Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
    but I should be able to easily change these values if I want.
    The output should say something like "You can make 9 omelettes with 6 boxes of eggs".
    """
    box = 1
    egg_per_box = 6
    egg_per_omelette = 4
    num_omelette = math.floor(box * egg_per_box / egg_per_omelette)
    print("You can make {} omelettes with {} boxes of eggs".format(num_omelette, box))


"""
Session 2
"""
def S2Q1():
    """
    Question 1
    Create a program that tells you whether or not you need an umbrella when you leave the house.
    The program should:
    1. Ask you if it is raining using input()
    2. If the input is 'y', it should output 'Take an umbrella'
    3. If the input is 'n', it should output 'You don't need an umbrella'
    """
    rain = ""
    while (rain != "y") and (rain != "n"):
        rain = input("Is it raining today? (y or n) ")
    if rain == "y":
        msg = "Take an umbrella"
    else:
        msg = "You don't need an umbrella"
    print(msg)


def S2Q2():
    """
    Question 2
    I'm on holiday and want to hire a boat.
    The boat hire costs £20 + a refundable £5 deposit.
    I've written a program to check that I can afford the cost, but something doesn't seem right.
    Have a look at my program and work out what I've done wrong
    my_money = input('How much money do you have? ')
    boat cost = 20 + 5
    if my_money < boat_cost:
    print('You can afford the boat hire')
    else:
    print('You cannot afford the board hire')
    """
    print("""
    my_money = input('How much money do you have? ')
    boat_cost = 20 + 5
    if my_money < boat_cost:
        print('You can afford the boat hire')
    else:
        print('You cannot afford the board hire')
    
    Problem 1: comparing string with integer."
    Problem 2: "I can afford" meaning my_money is more than boat_cost   
    """)
    my_money = int(input('How much money do you have? '))
    boat_cost = 20 + 5
    if my_money >= boat_cost:
        print('You can afford the boat hire')
    else:
        print('You cannot afford the board hire')



if __name__ == "__main__":
    S1Q1()
    S1Q2()
    S1Q3()

    S2Q1()
    S2Q2()
