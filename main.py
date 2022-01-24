import requests


def get_random(amount: int = 1):
    r = requests.get(f"https://random-word-api.herokuapp.com/word?number={amount}")
    return r.text.split("\"")[1]


def run():
    word = get_random()
    placeholder = "_"
    lives = 6
    done = False
    guess = placeholder * len(word)

    while not done:
        print("*"*30)
        print(f"Current guess: {guess}\nLives: {lives}")
        user_in = input("Enter your guess: ").lower()
        if user_in in word:
            for index, value in enumerate(word):
                if value == user_in:
                    s = list(guess)
                    s[index] = user_in
                    guess = "".join(s)
        else:
            lives -= 1

        if lives <= 0 or word == guess:
            done = True
            print("*" * 30)
            print(f"Game has ended\nThe word was {word}")


if __name__ == '__main__':
    run()
