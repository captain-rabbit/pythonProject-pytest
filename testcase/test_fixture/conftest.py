import pytest


@pytest.fixture(scope="session",autouse=True)
def test_session():
    print("我是session级的fixture")


@pytest.fixture(scope="function")
def func():
    print("我是前置步骤我需要先运行")
    yield
    print("我是后置步骤 我最后运行")

@pytest.fixture()
def get_mobile():
    mobile = "13456755448"
    return mobile
