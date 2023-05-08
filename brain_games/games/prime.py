import random
import prompt
import brain_games.cli


def prime_game():
    print('Welcome to the Brain Games!')
    print(f'Hello, {brain_games.cli.welcome_user()}!')
    count = 0

    while count < 3:
        num = random.randrange(1, 100)

        def IsPrime(num):
            d = 2
            while d * d <= num and num % d != 0:
                d += 1
            return d * d > num

        print(f"""Answer "yes" if given number is prime.
        Otherwise answer "no".\n
        Question: {num}""")
        answer = prompt.string('Your answer: ')
        if IsPrime(num) is True:
            result = 'yes'
        else:
                result = 'no'

        if (IsPrime(num) is True and answer == 'yes') or (IsPrime(num) is False and answer == 'no'):
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
# prime_game()