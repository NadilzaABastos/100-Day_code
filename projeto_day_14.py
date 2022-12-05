from art import logo
from art import vs
from game_data import data
import random


def fallowers (account):
    data_name = account["name"]
    data_descr = account["description"]
    data_country = account["country"]
    return f"{data_name} a {data_descr} from {data_country}"

def game(guess,qtd_followers_a,qtd_followers_b):
    if qtd_followers_a > qtd_followers_b:
        return guess == "a"
    else:
        return guess == "b"



def jogo():
    print(logo)
    score = 0
    game_is_not_over = True
    b = random.choice(data)

    while game_is_not_over :
        a = b
        b = random.choice(data)
        if a == b:
            b = random.choice(data)

        print(f"Compare A : {fallowers(a)}.")
        print(vs)
        print(f"Against B : {fallowers(b)} .")

        guess = str(input("Who has more followers Type 'A' or 'B' : ")).lower()
        qtd_followers_a = a["follower_count"]
        qtd_followers_b = b["follower_count"]
        answer = game(guess,qtd_followers_a,qtd_followers_b)

        if answer:
            score += 1
            print(f"You're right! Current score:{score}")
        else:
            game_is_not_over = False
            print(f"Sorry, that's wrong. Final score : {score}")

jogo()