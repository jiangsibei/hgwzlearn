import pytest

class Test_Mark():

    @pytest.mark.demo
    def test_mark_one(self):
        print("one case")
        assert 1==3
    @pytest.mark.smoke
    def test_mark_two(self):
        print("two case")
        assert 1==4

    #可以加两个标签
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_mark_thir(self):
        print("thir case")

    # -m    标签的匹配
    # pytest -m "demo" test_mark_demo.py      只运行一个有demo的
    # pytest -m "demo or smoke" test_mark_demo.py   有demo和smoke的的都运行
    # pytest -m "demo and smoke" test_mark_demo.py   运行有demo且有smoke的


    # -k   用例名字的匹配
    # pytest -k  "two"   test_mark_demo.py  运行用例名字中有two的

    # -x  遇到失败的就停止


    # --maxfail=num
    #pytest - -maxfail = 2 test_mark_demo.py

    # --collect-only  只收集用例,不会执行运行
    # pytest - -collect - only  test_mark_demo.py
