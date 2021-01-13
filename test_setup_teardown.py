import pytest
#类里面
class TestClass():

    def setup_class(self):
        print("setup_class:类里面的所有用例开始时执行")
    def teardown_class(self):
        print("tearndown_class:在类里所有用例执行的结束后打印")
    def setup_method(self):
        print("setup: 每个用例开始执行 ")

    def teardown_method(self):
        print("teardown: 每个用例执行结束时")
    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")


#类外面

def setup_function():
    print(" 类外面，用例开始的")
def teardown_function():
    print("类外面，用例结束的")
def test_three():
    print("test three")

def test_four():
    print("test four")

#最高级别，该文件运行时最开始、结束时运行的
def setup_module():
    print("setup_module:模块级别的，运行最开始")

def teardown_module():
    print("teardown_module:模块级别的，运行结束的时候")