import requests
import csv
from lxml import etree
import os

url = "http://www.piaofang.biz/"
my_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "www.piaofang.biz",
    "pragma": "no-cache",
    "referer": "https://cn.bing.com/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"
}
resp = requests.get(url, headers=my_headers)
resp.encoding = "gbk"
# print(resp.text)
page = etree.HTML(resp.text)
trs = page.xpath("//table/tr")[1:]
f = open("movies2.csv", mode="w", encoding="utf-8")

for tr in trs:
    num_list = tr.xpath("./td[1]/text()")
    num = "".join(num_list).strip()
    if "排行榜" in num:
        continue
    year_list = tr.xpath("./td[3]/text()")
    year = "".join(year_list).strip()
    if not year:
        continue
    cn_name = "".join(tr.xpath("./td[2]/a/text()")).strip()
    en_name = "".join(tr.xpath("./td[2]/span/text()")).strip()
    if not cn_name:
        continue
    if not en_name:
        continue
    money ="".join(tr.xpath("./td[6]//text()"))
    # 把数据保存到文件
    f.write(f'{num},{year},{cn_name},{en_name},"{money}"\n')

f.close()