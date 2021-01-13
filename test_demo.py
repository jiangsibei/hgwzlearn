import pytest

# class Test_demo():
#     def test_one(self):
#         a = 5
#         b = 1
#         assert a != b
#         print("这个第一个测试用列")
#
#     def test_two(self):
#         a = 5
#         b = 1
#         assert a != b
#         print("这个第一个测试用列")

def add_function(a,b):
    return  a+b

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(-1,-9,-10),(10000,10000,20000)],ids=["one","two","thiret"])

def test_add(a,b,expected):
    assert  add_function(a,b) == expected

@pytest.mark.parametrize("a",[1,3,5])
@pytest.mark.parametrize("b",[4,5,6])
def test_add_zuhe(a,b):
    print("测试组合：a=%s,b=%s"%(a,b))
    assert add_function(a, b) == a+b
