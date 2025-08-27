from random import shuffle

list = [1, 0, 0]

def shuffle_list(x):
    shuffle(x)
    return x

shuffled_list = shuffle_list(list)
print(shuffled_list)

def call_user():
    result = input("Guess where the red ball is! Please choose between \n 1 \n 2 \n 3")
    return int(result)

def check_answer(user_input, shuffled_list):
    answer = user_input - 1
    if shuffled_list[answer] == 1:
        return True
    else:
        return False

def play_game():
    print(list)
    print("-----shuffling-----")
    input = call_user()
    result = check_answer(input, shuffled_list)
    
    if result == True:
        print("Congrats, you guessed the correct cup!")
    else:
        print("Sorry, you guessed wrong...")

play_game()

