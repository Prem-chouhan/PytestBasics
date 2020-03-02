import pytest


@pytest.yield_fixture()
def setup():
    print("this url is opened")
    yield
    print("Browser is closed")


def test_loginbyemail(setup):
    print("This is simple login email function to test")


def test_loginbyfacebook(setup):
    print("This is simple login facebook  function to test")
