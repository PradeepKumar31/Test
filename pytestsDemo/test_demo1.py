#Any pytest file name should start with test_ or end with _test
#pytest method names should start with test
#Any code should wrapped in method only
#method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail to run tests but not report the result in output
#fixtures are used as setup and teardown methods for testcases- conftest file to generalize fixture and
#make it available to all test cases (fixture name into parameters of method)
#when you define fixture scope to class only, it will run once before class is initiated and at the end
#data driven and parameterization can be done with return statements in tuple format

#https://docs.google.com/spreadsheets/d/1EH1UJ9Qezgx_aZ0xim3KcVJUCEeR7A-7/edit#gid=606968566

import pytest


@pytest.mark.smoke


def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_GreetCreditCard():
    print("Good Morning")


def test_crossbow(crossbow):
    print(crossbow[1])




