import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram3():
    msg = "Hello"
    assert msg == "Hi", "Test failed string do not match"


def test_SecondCreditcard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


@pytest.fixture()
def setup():
    print("I will be execute first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")


