import pytest

from utils.read_data import read_data


@pytest.mark.parametrize("name",read_data()['heros_name_word'])
def test_parametrze_02(name):
    print(name)


