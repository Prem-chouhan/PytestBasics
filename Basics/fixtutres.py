import pytest


@pytest.yield_fixture()
def setup():
    print("This is executed always once before a method")
    yield
    print("This is executed always once After a method")


def test_method(setup):
    print("This is Method")


# @pytest.fixture()
# def setup():
#     print("This is executed always once before a method")
#
#
# def test_method(setup):
#     print("This is Method")
