import pytest


@pytest.mark.parametrize("key",["value"])
def test_parametrize_01(key):
    print("我是"+key)


#参数化时有多个数据时会依次将数据传入用例执行
@pytest.mark.parametrize("hero_name",["安其拉","小乔","黄忠"])
def test_parametrize(hero_name):
    print(hero_name)