import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Raul", "Shi", "RaulRaulAcademy.com"]


# Option 1
@pytest.fixture(params=["chrome", "firefox", "IE"])  # run each test multi param
def crossBrowser(request):
    return request.param


# # Option 2 - Send muly values in one single one
# @pytest.fixture(params=[("chrome", "Raul", "Basson"), ("firefox","eli") ,("IE","SS")])  # run each test multi param
# def crossBrowser(request):
#     return request.param