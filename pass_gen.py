from random import choice, choices, shuffle
import string
lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
numbers = list('0123456789')
symbols = list('!?@.,/\&*')
easy_whole_list = lower_case + numbers
medium_whole_list = easy_whole_list + upper_case
hard_whole_list = medium_whole_list + symbols

lengths = int(input('Enter the lengths of password between 5 and 12: '))
while lengths not in range(5,13):
    lengths = int(input('Enter the valid lengths of password: '))

difficult = input('Choose the difficulty of password: easy, medium or hard: ').lower()
while difficult not in ['easy', 'medium', 'hard']:
    difficult = input('Choose the valid difficulty of password: easy, medium or hard: ').lower()

password_amount = int(input('How many passwords do you require? From 1 to 100: '))
while password_amount not in range(1,101):
    password_amount = int(input('How many passwords do you require? From 1 to 100: '))


def print_pass(func):
    count = 1
    for num in range(password_amount):
        print(f'{count} password is {func()}')
        count += 1


def easy_pass():
    pass_base_easy = list(choice(lower_case) + choice(numbers))
    final_list_easy = pass_base_easy + choices(easy_whole_list, k=lengths - 2)
    shuffle(final_list_easy)
    return ''.join(final_list_easy)


def medium_pass():
    pass_base_medium = list(choice(lower_case) + choice(numbers) + choice(upper_case))
    final_list_medium = pass_base_medium + choices(medium_whole_list, k=lengths - 3)
    shuffle(final_list_medium)
    return ''.join(final_list_medium)


def hard_pass():
    pass_base_hard = list(choice(lower_case) + choice(numbers) + choice(upper_case) + choice(symbols))
    final_list_hard = pass_base_hard + choices(hard_whole_list, k=lengths - 4)
    shuffle(final_list_hard)
    return ''.join(final_list_hard)


if difficult == 'easy':
    print_pass(easy_pass)
elif difficult == 'medium':
    print_pass(medium_pass)
elif difficult == 'hard':
    print_pass(hard_pass)


