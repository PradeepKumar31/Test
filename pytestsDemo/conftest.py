import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be excuting first")
    yield
    print("I will be exceuted last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being  created")
    return ["rahul","shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","rahul","shetty",),("Firefox","Reha"),("IE","SS")])
def crossbow(request):
    return request.param
