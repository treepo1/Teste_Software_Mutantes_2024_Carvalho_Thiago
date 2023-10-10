import pytest
import pass_gen
from random import choice


@pytest.fixture()
def rand_pass(request):
    difficulty_range = choice(['easy', 'medium', 'hard'])
    length = choice(range(5, 13))
    obj = pass_gen.PassGen(length, difficulty_range)
    request.cls.obj = obj
    yield
    del obj


@pytest.fixture()
def rand_pass_list(request):
    amount_range = choice(range(1, 101))
    difficulty_range = choice(['easy', 'medium', 'hard'])
    length = choice(range(5, 13))
    obj = pass_gen.PassList(length, difficulty_range, amount_range)
    request.cls.obj = obj
    yield
    del obj


@pytest.fixture()
def rand_email_pass_dict(request):
    amount_range = choice(range(1, 101))
    difficulty_range = choice(['easy', 'medium', 'hard'])
    length = choice(range(5, 13))
    obj = pass_gen.EmailPassDict(length, difficulty_range, amount_range)
    request.cls.obj = obj
    yield
    del obj

