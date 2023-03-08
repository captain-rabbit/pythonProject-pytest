import pytest
import requests

from utils.read_data import get_data
from utils.read_ini import read_ini

#@pytest.mark.parametrize("param", get_data["mobile_belong"])
def test_mobile_get():
    param = get_data["mobile_belong"]
    r = requests.get('http://sellshop.5istudy.online/sell/shouji/query',
                     params={"shouji": param["shouji"], "appkey": param["appkey"]})
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["city"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"

url = read_ini()['host']['api_sit_url']
@pytest.mark.parametrize("shouji,appkey", get_data["mobile_belong_post"])
def test_mobile_post(shouji,appkey):
    params = {"shouji": shouji, "appkey": appkey}
    r = requests.post(url+'/sell/shouji/query', params=params)
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["city"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
