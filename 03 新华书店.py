"""
网址: https://search.xhsd.com/search?frontCategoryId=35
目标: 商品的标题, 价格, 标签, 简介
"""

import requests
import csv
from lxml import etree
# def get_one_page_data(url):
#     print("✅当前收到的url参数：", url)
url = "https://search.xhsd.com/search?frontCategoryId=35&display=1&pageNo=1"
my_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "cookie": "guestId=4ccec532-ff98-45a7-b48e-631c6bfe441c; taid=d31a7cdf-a486-449c-9eee-0dc4e203870a; sajssdk_2015_cross_new_user=1; UM_distinctid=1a05ad8ccff548-041baa5ab7521f8-26011c51-10c13a-1a05ad8cd004f3; aliyungf_tc=34534ee1a2f0c69c5735427ed1750d809c186d3efff24f2a50a858004477c192; msid=tLoLvABWVTiUpv5LfjZyn7f8xE9BIkBY; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221a05ad8ccd51a1-022e5a99cf8a022-26011c51-1098042-1a05ad8ccd62ed%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMWEwNWFkOGNjZDUxYTEtMDIyZTVhOTljZjhhMDIyLTI2MDExYzUxLTEwOTgwNDItMWEwNWFkOGNjZDYyZWQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a05ad8ccd51a1-022e5a99cf8a022-26011c51-1098042-1a05ad8ccd62ed%22%7D; acw_tc=781bad5817882539069118633e00b8d1c609afc950b89337a4def96ce0d617; CNZZDATA1274306588=1579734600-1788230560-https%253A%252F%252Fwww.xhsd.com%252F%7C1788253908",
    "host": "search.xhsd.com",
    "referer": "https://search.xhsd.com/search?frontCategoryId=35&display=1&pageNo=3",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=my_headers)
    # print(resp.text)
    # 对数据进行解析
tree = etree.HTML(resp.text)
lis = tree.xpath(".//ul[@class='shop-search-items-img-type']/li")
        # print(len(lis))  #看下有多少组数据
f = open(f"./book.csv", mode="w", encoding="utf-8")
for li in lis:
        #标题
    title = "".join(li.xpath(".//p[@class='product-desc']/a/text()"))
    price = ''.join(li.xpath(".//p[@class='product-price ']/span/text()"))
    author = ''.join(li.xpath(".//p[@class='product-author ']/span/text()"))
    s = f"{title},{price},{author}"
    f.write(s)
    f.write("\n")
    print(s)
f.close()
# def main():
#     for i in range(1,11):
#         if i == 1:
#             url = "https://search.xhsd.com/search?frontCategoryId=35&display=1&pageNo=1"
#         else:
#             url = f"https://search.xhsd.com/search?frontCategoryId=35&display=1&pageNo={i}"
#         get_one_page_data(url)
#         print(f"=============第{i}页的数据抓取完毕")
#
# if __name__ == '__main__':
#     main()
# def main():
#     for i in range(0,1):
#         # 简化！不需要if else，一行生成所有页码url
#         url = f"https://search.xhsd.com/search?frontCategoryId=35&display=1&pageNo={i}"
#         get_one_page_data(url)
#         print(f"=============第{i}页的数据抓取完毕")
#
# if __name__ == '__main__':
#     main()