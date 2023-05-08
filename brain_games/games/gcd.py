import random
import prompt
import brain_games.cli
from math import gcd


def gcd_game():
    print('Welcome to the Brain Games!')
    print(f'Hello, {brain_games.cli.welcome_user()}!')
    count = 0

    while count < 3:
        num1 = random.randrange(1, 20)
        num2 = random.randrange(1, 20)
        result = gcd(num1, num2)

        print(f"""Find the greatest common divisor of given numbers.\n
        Question: {num1} {num2}""")
        answer = prompt.integer('Your answer: ')

        if int(answer) == int(result):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {brain_games.cli.user_name}!')
        else:
            print(f"""'{answer}' is wrong answer ;(.
            Correct answer was {result} \n
            Let's try again, {brain_games.cli.user_name}!""")
            count = 0
            break
