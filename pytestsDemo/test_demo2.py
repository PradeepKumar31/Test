#Any pytest file name should start with test_ or end with _test
#pytest method names should start with test
#Any code should wrapped in method only
#method name should have sense
#-k stands for method names execution, -s logs in output, -v stands for more info metadata
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and teardown mthods for test cases - conftest file to generalize fixture
#and make it available to all test cases
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"  # this 2nd string will only print if assert fails

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"


