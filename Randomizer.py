"""
Język programowania Python

Projekt: Randomizer
Marta Zawadzka

"""

import random

def first_clue(n):
    is_prime_num = 0
    if (n%2==0 or n%3==0 or n%5==0) and n!=2 and n!=3 and n!=5:
        is_prime_num = 0
    elif n==1:
        is_prime_num = 0
    else:
        is_prime_num = 1

    if is_prime_num:
        print("Number to guess is prime number.")
    else:
        print("Number to guess is not a prime number.")


def second_clue(_num_to_guess):
    if _num_to_guess%2==0:
        print("Number to guess is even.")
    else:
        print("Number to guess is odd.")


def third_clue(_num_to_guess):
    if _num_to_guess%3==0:
        print("Number to guess is divisible by 3.")
    else:
        print("Number to guess is not divisible by 3.")


def fourth_clue(_num_to_guess):
    if _num_to_guess>=0 and _num_to_guess<=50:
        print("Number to guess is from first half of range.")
    else:
        print("Number to guess is from second half of range.")


def any_clue(num, _num_to_guess):
    if num > _num_to_guess:
        print("You should type smaller number.")
    else:
        print("You should type bigger number.")

def invoking_clues_func(num, _num_to_guess, func_num):
    if func_num==1:
        first_clue(_num_to_guess)
    if func_num==2:
        second_clue(_num_to_guess)
    if func_num==3:
        third_clue(_num_to_guess)
    if func_num==4:
        fourth_clue(_num_to_guess)
    elif func_num>4:
        any_clue(num, _num_to_guess)


def random_num_game():
    score = 101
    your_num = -100
    i = 1
    i_clipboard = i
    rand_num = random.randint(0,100)
    print("Guess a number (from 0 to 100): ")
    while(your_num != rand_num):
        try:
            invoking_clues_func(your_num, rand_num, i)
        except Exception as e:
            i = i_clipboard
            print("Error: not a natural number\n", e)
        except ArithmeticError:
            i = i_clipboard
            print("Arithmetic Error")
        score = score - 1
        try:
            your_num=input()
            your_num = int(your_num)
        except Exception as e:
            i = i_clipboard
            print("Error: not a natural number\n", e)
        except ArithmeticError:
            i = i_clipboard
            print("Arithmetic Error")

        i_clipboard = i
        i += 1

    print("Number to guess: " + str(rand_num))
    print("Your number: " + str(your_num))
    print("Your score: " + str(score) + " out of 100")


if __name__=="__main__":
    keep_playing = "1"
    while(keep_playing == "1"):
        random_num_game()
        print("If you want to play again type 1. Else, type anything.")
        keep_playing = input()