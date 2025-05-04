# Test for problem_238
from solutions.problem_238 import product_except_self

def test_problem_238():
    assert product_except_self(nums=[1,2,3,4]) == [24,12,8,6]
