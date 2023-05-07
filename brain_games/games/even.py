import random
import prompt
import brain_games.cli


def even_game():
    print('Welcome to the Brain Games!')
    print(f'Hello, {brain_games.cli.welcome_user()}!')
    count = 0

    while count < 3:
        number = random.randrange(1, 100)
        print(f"""Answer "yes" if the number is even, otherwise answer "no".\n
        Question: {number}""")
        answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {brain_games.cli.user_name}!')
        else:
            print(f"""Let's try again, {brain_games.cli.user_name}!""")
            break

# even_game()
# '{answer}' is wrong answer ;(. \n