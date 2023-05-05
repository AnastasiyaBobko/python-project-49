import random
import prompt
import brain_games.cli


def calc_game():
    print('Welcome to the Brain Games!')
    print(f'Hello, {brain_games.cli.welcome_user()}!')
    count = 0

    while count < 3:
        char = random.choice('+-*')
        num1 = random.randrange(1, 20)
        num2 = random.randrange(1, 20)
        resul = ''
        if char == '+':
            result = num1 + num2
        elif char == '-':
            result = num1 - num2
        else:
            result = num1*num2
        print(f"""What is the result of the expression?\n
        Question: {num1} {char} {num2}""")
        answer = prompt.string('Your answer: ')
        
        if int(answer) == int(result):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {brain_games.cli.user_name}!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer is {result} \n
            Let's try again, {brain_games.cli.user_name}!""")




