import json

import requests


url = "https://reading.sc.lnep.net/m/tkreader/Handler/TKHandler.ashx"

def get_params(questionPlanID,paperID):
    return {
    "method": "GetQustionsForH5",
    "questionPlanID": questionPlanID,
    "paperID": paperID
}
headers = {
    "Host": "reading.sc.lnep.net",
    "Connection": "keep-alive",
    "sec-ch-ua": "Microsoft Edge;v=125, Chromium;v=125, Not.A/Brand;v=24",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://reading.sc.lnep.net/tkReader/tk/TkReader.aspx?questionPlanID=4363&From=Ebook&UserName=18873474740&token=et0O4NklBrnL6A1pJ%2bjidsi%2fqk816hecsTl6Au6DzdcT70yiC%2bS3aQ%3d%3d",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie": "ASP.NET_SessionId=ctnkgnzhwfwjdlrhqyrqsxba; Hm_lvt_10516055fe68303d2ae0d8cfe734ceb3=1717920604; Hm_lpvt_10516055fe68303d2ae0d8cfe734ceb3=1717920690"
}

def get_questionId(questionPlanID,paperID):
    try:
        response = requests.get(url, headers=headers,params=get_params(questionPlanID,paperID))
        if response.status_code==200:

            data=response.json()
            nodeList=data["data"]["nodeList"]
            questionId=[e["questionId"] for each in nodeList for e in each["questionLists"]]

            return True,questionId
        else:
            return False,response.status_code
    except:
        return False,None