import pytest

#数据结构可以是数组元组或字典
#数组形式
# @pytest.mark.parametrize("name,word",[["安其拉","火炎"],["小乔","甜蜜"],["黄忠","射"]])
# def test_parametrze_02(name,word):
#     print(f'{name}的台词有{word}')

#字典形式
@pytest.mark.parametrize("hero",[{"name":"安其拉","word":"火炎"},{"name":"小乔","word":"甜蜜"},{"name":"黄忠","word":"射"}])
def test_parametrze_02(hero):
    print(hero["name"])
    print(hero["word"])


