import  pytest
import yaml


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["ids"]
        return [add_datas, add_ids]


class TestDataYmlClass():

    @pytest.mark.parametrize("a,b,execpt", yaml.safe_load(open("./data.yml"))["datas"],ids=yaml.safe_load(open("./data.yml"))["ids"])
    def test_add(self,a,b,execpt):
        assert a+b==execpt

    #使用打开文件的函数
    @pytest.mark.parametrize("a,b,execpt", get_datas()[0],ids = get_datas()[1])
    def test_add1(self, a, b, execpt):
        assert a + b == execpt