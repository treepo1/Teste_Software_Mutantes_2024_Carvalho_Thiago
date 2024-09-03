#Only unit tests with using conftest.py are presented here
import pass_gen
import pytest


@pytest.mark.usefixtures('rand_pass')
class TestPassGen:
    @pytest.mark.parametrize('length_pos', [5, 8, 12])
    def test_length_(self, length_pos):
        self.obj.length = length_pos
        assert len(self.obj.get_pass()) == length_pos

    def test_difficult_easy(self):
        self.obj.difficult = 'easy'
        for el in self.obj.get_pass():
            assert el in pass_gen.PassGen.EASY_WHOLE_LIST

    def test_difficult_medium(self): 
        self.obj.difficult = 'medium'
        for el in self.obj.get_pass():
            assert el in pass_gen.PassGen.MEDIUM_WHOLE_LIST

    def test_difficult_hard(self):
        self.obj.difficult = 'hard'
        for el in self.obj.get_pass():
            assert el in pass_gen.PassGen.HARD_WHOLE_LIST


@pytest.mark.usefixtures('rand_pass')
class TestPassGenNegative:
    @pytest.mark.parametrize('length_neg', [4, 13])
    def test_length(self, length_neg):
        self.obj.length = length_neg
        with pytest.raises(ValueError):
            self.obj.get_pass()

    @pytest.mark.parametrize('length_neg', [4, 13])
    def test_length_init(self, length_neg):
        with pytest.raises(ValueError,match=r"Length should be between 5 and 12$"):
            self.obj.__init__(length_neg, "easy")

    def test_difficult_wrong(self):
        self.obj.difficult = 'qwerty'
        with pytest.raises(ValueError):
            self.obj.get_pass()

    def test_difficult_wrong_init(self):
        difficult = 'qwerty'
        with pytest.raises(ValueError, match=r"Difficult should be easy, medium or hard$"):
            self.obj.__init__(6,difficult)


@pytest.mark.usefixtures('rand_pass_list')
class TestPassSequence: 
    @pytest.mark.parametrize('amount', [1, 50, 100])
    def test_amount_pos(self, amount):
        self.obj.amount = amount
        assert len(self.obj.get_pass_list()) == amount

    @pytest.mark.parametrize('amount', [0, 101])
    def test_amount_neg(self, amount):
        self.obj.amount = amount
        with pytest.raises(ValueError):
            self.obj.get_pass_list()

    @pytest.mark.parametrize('amount', [0, 101])
    def test_amount_neg_init(self, amount):
        with pytest.raises(ValueError,match=r"Amount should be between 1 and 100$"):
            self.obj.__init__(6, "easy", amount)

@pytest.mark.usefixtures('rand_email_pass_dict')
class TestPassEmailDict:
    def test_email(self):
        for el in self.obj.get_email_pass_dict():
            assert '@fakemail.com' in el

    def test_email_len(self):
        for el in self.obj.get_email_pass_dict():
            assert len(el.replace('@fakemail.com', '')) in range(5, 8)




