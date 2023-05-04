import prompt


user_name = ''


def welcome_user():
    global user_name
    user_name = prompt.string('May I have your name? ')
    return user_name
