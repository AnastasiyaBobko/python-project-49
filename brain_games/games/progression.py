import random
import prompt
import brain_games.cli


def progression_game():
    print('Welcome to the Brain Games!')
    print(f'Hello, {brain_games.cli.welcome_user()}!')
    count = 0

    while count < 3:
        start_num = random.randrange(1, 10)
        step_num = random.randrange(1, 5)
        stop_num = random.randrange(10, 60)
        list_numbers = list(range(start_num, stop_num, step_num))
        index_num = random.randrange(len(list_numbers))
        number = list_numbers[index_num]
        list_numbers[index_num] = '..'

        print(f"""What number is missing in the progression?\n
        Question: {' '.join(map(str, list_numbers))}""")
        answer = prompt.integer('Your answer: ')

        if int(answer) == int(number):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {brain_games.cli.user_name}!')
        else:
            print(f"""'{answer}' is wrong answer ;(.
            Correct answer was {number} \n
            Let's try again, {brain_games.cli.user_name}!""")
            count = 0
            break
