from random import choice, choices, shuffle
import string


class PassGen:
    LOWER_CASE = list(string.ascii_lowercase)
    UPPER_CASE = list(string.ascii_uppercase)
    NUMBERS = list('0123456789')
    SYMBOLS = list('!?@&*')
    EASY_WHOLE_LIST = LOWER_CASE + NUMBERS
    MEDIUM_WHOLE_LIST = EASY_WHOLE_LIST + UPPER_CASE
    HARD_WHOLE_LIST = MEDIUM_WHOLE_LIST + SYMBOLS

    def __init__(self, length, difficult):
        if length in range(5, 13):
            self.length = length
        else:
            raise ValueError('Length should be between 5 and 12')
        if difficult in ('easy', 'medium', 'hard'):
            self.difficult = difficult
        else:
            raise ValueError('Difficult should be easy, medium or hard')

    def __easy_pass(self):
        """"Create base with one random lower case letter and one random number from 0 to 9,
        add to this base (user input length - 2(two elements are already used in base)) amount of random elements
        from mixed list of lower case letters and  numbers, shuffle it and return a string"""
        pass_base_easy = list(choice(self.LOWER_CASE) + choice(self.NUMBERS))
        final_list_easy = pass_base_easy + choices(self.EASY_WHOLE_LIST, k=self.length - 2)
        shuffle(final_list_easy)
        return ''.join(final_list_easy)

    def __medium_pass(self):
        pass_base_medium = list(choice(self.LOWER_CASE) + choice(self.NUMBERS) + choice(self.UPPER_CASE))
        final_list_medium = pass_base_medium + choices(self.MEDIUM_WHOLE_LIST, k=self.length - 3)
        shuffle(final_list_medium)
        return ''.join(final_list_medium)

    def __hard_pass(self):
        pass_base_hard = list(choice(self.LOWER_CASE) + choice(self.NUMBERS) +
                              choice(self.UPPER_CASE) + choice(self.SYMBOLS))
        final_list_hard = pass_base_hard + choices(self.HARD_WHOLE_LIST, k=self.length - 4)
        shuffle(final_list_hard)
        return ''.join(final_list_hard)

    def __create_pass(self):
        """return password string of user choice: easy, medium or hard"""
        if self.difficult == 'easy':
            return self.__easy_pass()
        elif self.difficult == 'medium':
            return self.__medium_pass()
        elif self.difficult == 'hard':
            return self.__hard_pass()
        else:
            raise ValueError

    def get_pass(self):
        """return a string with password, in case of length reassignment with
         invalid value(not between 5 and 13) raise ValueError"""
        if len(self.__create_pass()) in range(5, 13):
            return self.__create_pass()
        else:
            raise ValueError


class PassList(PassGen):
    def __init__(self, length, difficult, amount):
        super().__init__(length, difficult)
        if amount in range(1, 101):
            self.amount = amount
        else:
            raise ValueError('Amount should be between 1 and 100')

    def __create_pass_list(self):
        return [self.get_pass() for self.p in range(self.amount)]

    def get_pass_list(self):
        if len(self.__create_pass_list()) in range(1, 101):
            return self.__create_pass_list()
        else:
            raise ValueError


class EmailPassDict(PassList):
    def email(self):
        return ''.join(choices(self.LOWER_CASE, k=choice(range(5, 8)))) + '@fakemail.com'

    def get_email_pass_dict(self):
        return {self.email(): password for password in self.get_pass_list()}
