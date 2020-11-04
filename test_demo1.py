import pytest

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")


@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SeconGreetCreditCard():
    print("Good Morning")

# op 1
# def test_crossBrowser(crossBrowser):
#     print(crossBrowser)

# op 2
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
