# import statements
from random import randrange, sample

# program Structure

game_status = {
    "home": {},
    "away": {}
}

game_name = "Commander Shagmar"
game_ins = """ 
The goal of the game is to capture the most objectives.
To successfully capture an objective, you need to dedicate more soldiers than your opponent.
In each battle you only have a 100 soldiers and you need to distribute the soldiers among 3 objectives. 
Still dont understand ? Just start playing to get a hang of it.

"""
# round_count initialization
round_count = 0


# function to update dictionary value while playing
def update_status(a, b):
    global round_count
    game_status["home"][round_count] = a
    game_status["away"][round_count] = b
    round_count += 1


# welcome message function; takes user_name, string of user_name as input
def welcome_msg(user_name):
    response = input(f"Hello {user_name}. Welcome to {game_name} !! Have you played before ? Print Y/N")

    if response == "Y" or response == "y":
        print("Great, im sure you know the rules")

    elif response == "N" or response == "n":
        print(game_ins)
        res = input("press any key to continue")

    else:
        print("invalid response")
        welcome_msg(user_name)


# automated_enemy creation using random module. y is number of rounds, num is number of soldiers
def automated_enemy(y, num):
    empty = []
    initial = num
    holder = 0
    for x in range(y):

        if x == y - 1:
            n = initial - sum(empty)
            empty.append(n)

        else:
            num = num - holder
            n = randrange(0, num + 1)
            empty.append(n)
            holder = n

    enemy_list = sample(empty, len(empty))
    return enemy_list


def game_state(name, bat):
    battles = bat
    soldiers = 100

    home_results = []

    # battle results function to print result of battle.Takes in dictionary as data parameter and debug boolean to help diagnose if needed
    def battle_results(data, debug, user_name):
        # Initialize h_score_rnd and a_score_rnd
        h_score_rnd = a_score_rnd = 0

        # loop through home and away scores with round as index. Assign winner in each objective. then winner in each round

        # loop through Dictionary; "home" and "away"
        for i in data:
            # loop through round
            for x in data[i]:
                # Initialize "h_score_obj" and "a_score_obj"
                h_score_obj = a_score_obj = 0
                # Loop through individual objs
                for y in range(3):
                    # Debug statement
                    if debug:
                        print("round", y)

                    if data["home"][x][y] > data["away"][x][y]:
                        h_score_obj += 1

                        # Debug statement
                        if debug:
                            print("home winner", data["home"][x][y], data["away"][x][y])
                            print(i, x, y)
                            print("home score is", h_score_obj, "\n")

                    elif data["home"][x][y] < data["away"][x][y]:
                        a_score_obj += 1

                        # Debug statement
                        if debug:
                            print("away winner", data["home"][x][y], data["away"][x][y])
                            print(i, x, y)
                            print("away score is", a_score_obj, "\n")

                # Round score calculations
                if h_score_obj > a_score_obj:
                    h_score_rnd += 1

                elif h_score_obj < a_score_obj:
                    a_score_rnd += 1

                # Debug statement
                if debug:
                    print("round score")
                    print(h_score_rnd, a_score_rnd, "\n")

        # Debug statement
        if debug:
            print(h_score_rnd, a_score_rnd)

        # Winner calculation based on round score
        if h_score_rnd > a_score_rnd:
            print(f"{user_name} Wins")

        elif h_score_rnd < a_score_rnd:
            print("Computer Wins")

    for bat in range(battles):
        # First objective
        # Using hold to control program continuation
        hold = True
        while hold:
            print(f"Commander {name}, welcome to battle {bat + 1}")

            # Try ans except to prevent Value error
            try:
                num = int(
                    input(
                        F"General: Supreme Commander {name}, you've reached objective 1, how many soldiers do we send"))
            except ValueError:
                print("Please enter a whole number\n")
                continue

            # statement if soldier count is more than 100
            if num > 100:
                print("You only have 100 soldiers")
            else:
                home_results.append(num)
                hold = False

        # Second objective

        # Using hold to control program continuation
        hold = True
        while hold:
            try:
                num1 = int(input(
                    f"General: Supreme Commander {name}, you've reached objective 2, we have {soldiers - sum(home_results)} left, how many soldiers do we send"))
            except ValueError:
                print("Please enter a whole number\n")
                continue

            k = sum(home_results)

            if num1 > (soldiers - k):
                print("That's more than we have")
                print(f"soldier count: {soldiers - sum(home_results)}")

            else:
                home_results.append(num1)
                hold = False

        # Third objective

        # Using hold to control program continuation
        hold = True
        while hold:
            try:
                num2 = int(input(
                    F"General: Supreme Commander {name}, you've reached objective 3, we have {soldiers - sum(home_results)} left, how many soldiers do we send"))
            except ValueError:
                print("Please enter a whole number\n")
                continue

            k = sum(home_results)

            if num2 > (soldiers - k):
                print("That's more than we have")
                print(f"soldier count: {soldiers - sum(home_results)}")

            else:
                home_results.append(num2)
                hold = False

        player2 = automated_enemy(battles, soldiers)

        def round_results():
            global result
            h_score = 0
            a_score = 0

            for x in range(len(home_results)):

                if player2[x] < home_results[x]:

                    print(f"General: Commander {name}, We've taken victory at objective {x + 1}")
                    h_score += 1

                elif player2[x] > home_results[x]:
                    print(f"General: Commander {name}, We've lost at objective {x + 1}")
                    a_score += 1
                    # away_score = away_score + 1

                elif player2[x] == home_results[x]:
                    print(f"General: Commander {name}, its a stand still at objective{x + 1}")

                if h_score > a_score:
                    result = "Congratulations we won this battle !"
                elif a_score > h_score:
                    result = "Unfortunately we lost this battle"
            print(
                f"\n{result} \nWe sent {home_results[0]} to objective 1 our opponents sent {player2[0]} \nWe sent {home_results[1]} to objective 2 our opponents sent {player2[1]}\nWe sent {home_results[2]} to objective 3 our opponents sent {player2[2]} \n")

        round_results()
        update_status(home_results, player2)
        home_results = []
        home_score = 0
        away_score = 0
    battle_results(game_status, False, name)


##################################################################################
name = input("Name your character")

welcome_msg(name)

game_state(name, 3)
#print(game_status)
print("Thank you for playing commander Shagmar. Visit nitrokilo.com for more cool stuff")


