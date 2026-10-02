"""
网址: http://www.boxofficecn.com/boxofficecn
目标: 大陆所有的电影票房信息
"""

import requests
from lxml import etree
import os


def get_movie_by_year(year):
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    my_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1721017730,1721633285,1721992258; HMACCOUNT=40D17769013D04CF; __51cke__=; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1721995895; __tins__4287866=%7B%22sid%22%3A%201721994641409%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201721997694523%7D; __51laig__=4",
        "dnt": "1",
        "host": "www.boxofficecn.com",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=my_headers)
    # print(resp.text)

    # 解析html. 获取到需要的数据
    page = etree.HTML(resp.text)
    trs = page.xpath("//table/tbody/tr")[1:]  # 每一行

    # 杀头的罪过...
    f = open(f"./movies/{year}.csv", mode="w", encoding="utf-8")

    for tr in trs:  # 循环出每一行
        num = "".join(tr.xpath("./td[1]//text()"))
        if not num:     # num如果取不到. 直接过滤掉该数据
            continue
        year = "".join(tr.xpath("./td[2]//text()"))  # 这里的0建议大家改成join
        if not year:
            continue
        name = "".join(tr.xpath("./td[3]//text()"))
        money = "".join(tr.xpath("./td[4]//text()"))

        s = f"{num},{year},{name},{money}"
        # 把数据保存到文件
        f.write(s)
        f.write("\n")
    f.close()


# 创建文件夹
if not os.path.exists("./movies"):
    os.makedirs("./movies")

for year in range(1994, 2025):  # 20W
    get_movie_by_year(year)
    print(f"{year}年的数据已经保存完毕!")
