import requests


def get_headers(questionPlanID):
    return {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": f"https://reading.sc.lnep.net/tkReader/tk/TkReader.aspx?questionPlanID={questionPlanID}&UserName=18873474740&PackageId=968345&fromplat=&token=et0O4NklBrkl5XO0%2b0ezZXfSBUQTg0ASRvZgIDIzZxt%2fbPYZtIx6Lg%3d%3d",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "Microsoft Edge;v=125, Chromium;v=125, Not.A/Brand;v=24",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
cookies = {
    "ASP.NET_SessionId": "ctnkgnzhwfwjdlrhqyrqsxba",
    "Hm_lvt_10516055fe68303d2ae0d8cfe734ceb3": "1717920604",
    "Hm_lpvt_10516055fe68303d2ae0d8cfe734ceb3": "1717921379"
}
def get_params(tkid,paperid,qid):
    return {
    "method": "GetQuestionDetailForH5",
    "tkid": tkid,
    # tkid是题库id,questionId也是
    "paperid": paperid,
    "qid": qid
#
}
def GetQuestionDetailForH5(tkid,paperid,qid):

    url = "https://reading.sc.lnep.net/m/tkreader/Handler/TKHandler.ashx"
    try:
        response = requests.get(url, headers=get_headers(tkid), cookies=cookies, params=get_params(tkid,paperid,qid))
        if response.status_code==200:
            data=response.json()
            if data["result"]==-1:
                return False,None
            return True,data["data"]
        else:
            return False,None
    except:
        return False,None

if __name__ == '__main__':
    flag,result=GetQuestionDetailForH5(2668,"be4bda79-0099-4886-ac7d-3b6cd6b8b7cd" ,
                                       "5f1f31d6-05cd-4655-baa9-1060d9336c91")
    print(result)