import pytest


@pytest.yield_fixture()
def setup():
    print("this url is opened")
    yield
    print("Browser is closed")


def test_Signupbyemail(setup):
    print("This is simple Sign Up email function to test")


def test_signupbyfacebook(setup):
    print("This is simple Sign Up facebook  function to test")
