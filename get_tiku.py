import requests


# 获取各个题库的paperid
def get_tiku(tkid):
    url = "https://reading.sc.lnep.net/m/tkreader/Handler/TKHandler.ashx"
    params = {
        "method": "GetMenu",
        "tkid": str(tkid),
        "qtID": "",
        "islib": "0"
    }
    response = requests.get(url, params=params)
    json_data=response.json()

    paperList=list(filter(lambda x:x["paperList"] if x.get("paperList",None) else None,json_data["data"]))
    return paperList
if __name__ == '__main__':
    get_tiku(1000)
    # for x in range(1):
    #     pass