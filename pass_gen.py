from random import choice, choices, shuffle
import string


class PassGen:
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    numbers = list('0123456789')
    symbols = list('!?@.,/\&*')
    easy_whole_list = lower_case + numbers
    medium_whole_list = easy_whole_list + upper_case
    hard_whole_list = medium_whole_list + symbols

    def __init__(self, lengths=5, difficult='easy', amount=1):
        self.lengths = lengths  # Enter the lengths of password between 5 and 12
        self.difficult = difficult  # Choose the difficulty of password: easy, medium or hard
        self.amount = amount  # Choose amount of passwords


class PassCreate(PassGen):
    def easy_pass(self):
        pass_base_easy = list(choice(self.lower_case) + choice(self.numbers))
        final_list_easy = pass_base_easy + choices(self.easy_whole_list, k=self.lengths - 2)
        shuffle(final_list_easy)
        return ''.join(final_list_easy)

    def medium_pass(self):
        pass_base_medium = list(choice(self.lower_case) + choice(self.numbers) + choice(self.upper_case))
        final_list_medium = pass_base_medium + choices(self.medium_whole_list, k=self.lengths - 3)
        shuffle(final_list_medium)
        return ''.join(final_list_medium)

    def hard_pass(self):
        pass_base_hard = list(choice(self.lower_case) + choice(self.numbers) +
                              choice(self.upper_case) + choice(self.symbols))
        final_list_hard = pass_base_hard + choices(self.hard_whole_list, k=self.lengths - 4)
        shuffle(final_list_hard)
        return ''.join(final_list_hard)


class EmailCreate(PassGen):
    def email(self):
        return ''.join(choices(self.lower_case, k=choice(range(5, 8)))) + '@fakemail.com'


class GetPass(PassCreate, EmailCreate):
    def get_pass(self):
        if self.difficult == 'easy':
            return {self.email(): self.easy_pass() for x in range(self.amount)}
        elif self.difficult == 'medium':
            return {self.email(): self.medium_pass() for x in range(self.amount)}
        else:
            return {self.email(): self.hard_pass() for x in range(self.amount)}


