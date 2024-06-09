import requests
import tqdm

from lxml import etree

xpath_link="//div[@class='ItemName']/a/@href"
xpath_text="//div[@class='ItemName']/a/text()"

# 此脚本用于收集planid的所有书籍

def parse(html):
    tree=etree.HTML(html)

    links=tree.xpath(xpath_link)
    text_ls=tree.xpath(xpath_text)

    return links,text_ls

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.100xuexi.com/tklist/index.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "sec-ch-ua": "Microsoft Edge;v=125, Chromium;v=125, Not.A/Brand;v=24",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
cookies = {
    "JG_c08baa8ab281d77937fb84541_PV": "1717920545103|1717920545103",
    "HWWAFSESTIME": "1717920455233",
    "HWWAFSESID": "a2c40792840c6750a4",
    "Hm_lvt_31542562152130f4d571e37127af4555": "1717920459",
    "www.echatsoft.com_531632_encryptVID": "Tv1BN0ehPSUwA0qPg9RPpw%3D%3D",
    "www.echatsoft.com_531632_chatVisitorId": "4010503517",
    "xinreniftcount": "1",
    "echat_firsturl": "--1",
    "echat_firsttitle": "--1",
    "echat_referrer_timer": "echat_referrer_timeout",
    "echat_referrer": "--1",
    "echat_referrer_pre": "",
    "ECHAT_531632_web4010503517_miniHide": "0",
    "XX_UserId": "5XcKOyhI1qvwgpeGojTbQY3xNkLnCBdnVh6ul5PqrllucrQVLToIcQ==",
    "XX_UserNo": "a0zBx+4NVm7DKvo0A8pj1NiMmYKjbuDQk5/NsMfoWbCr3z746XVsxg==",
    "ASP.NET_SessionId": "uqqgzpjosjb1fqpoukmow50p",
    "XX_A_AllUserId": "nHhD1yrg507MvuARtLMwSQ==",
    "ECHAT_531632_webvip11734577_miniHide": "0",
    "Hm_lpvt_31542562152130f4d571e37127af4555": "1717933304"
}
for x in tqdm.tqdm(range(1,17)):
    url = f"https://www.100xuexi.com/tklist/1498/{x}.html"
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code==200:
        links, text_ls=parse(response.text)
        with open("./save_dir/record.json","a",encoding="utf-8") as f:
            f.write("\n".join(links))
            f.write("\n")