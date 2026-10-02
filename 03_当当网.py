"""
网址: https://category.dangdang.com/cp01.01.02.00.00.00.html
目标: 商品的标题, 价格, 标签, 简介
"""

import requests
from lxml import etree

def get_one_page_data(url):
    # url = "https://category.dangdang.com/cp01.01.02.00.00.00.html"

    my_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "ddscreen=2; __permanent_id=20240726191117926171491811049748828; __visit_id=20240726211347651337118592205683980; __out_refer=; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __rpm=s_605253.451684912835%2C451684912836..1721999633656%7Cs_605253.451684912835%2C451684912836..1721999642209; search_passback=277100891a762cd21aa1a36600000000a83168000ca1a366; __trace_id=20240726211402854272999889831347686; pos_9_end=1721999642915; ad_ids=2533482%2C3618801%2C2723440%2C2533488%7C%233%2C3%2C3%2C1; pos_6_end=1721999642965; pos_6_start=1721999855272",
        "dnt": "1",
        "host": "category.dangdang.com",
        "pragma": "no-cache",
        "referer": "https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    resp = requests.get(url, headers=my_headers)

    tree = etree.HTML(resp.text)

    lis = tree.xpath(".//div[@id='search_nature_rg']/ul/li")

    for li in lis:

        # 标题
        title = "".join(li.xpath("./p[@name='title']/a/text()")).strip()
        # 价格, 现在的价格, 划线价格
        now_price = "".join(li.xpath(".//span[@class='search_now_price']//text()"))
        # 有的价格没有划线价的. 只有一个xxxx起
        if "-" in now_price:
            now_price = now_price.split("-")[0].strip()
        pre_price = "".join(li.xpath(".//span[@class='search_pre_price']//text()"))
        if not pre_price:
            pre_price = "-"  # 根据客户的要求来弄...

        detail = "".join(li.xpath('./p[@class="detail"]//text()'))

        author = "".join(li.xpath("./p[@class='search_book_author']/span[1]//text()")).replace("/", "").strip()
        year = "".join(li.xpath("./p[@class='search_book_author']/span[2]//text()")).replace("/", "").strip()
        chu = "".join(li.xpath("./p[@class='search_book_author']/span[3]//text()")).replace("/", "").strip()
        print(title[:10], author, year, chu)



def main():
    # 第一次抓取. 抓取页码....
    url = "https://category.dangdang.com/cp01.01.02.00.00.00.html"
    my_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "ddscreen=2; __permanent_id=20240726191117926171491811049748828; __visit_id=20240726211347651337118592205683980; __out_refer=; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __rpm=s_605253.451684912835%2C451684912836..1721999633656%7Cs_605253.451684912835%2C451684912836..1721999642209; search_passback=277100891a762cd21aa1a36600000000a83168000ca1a366; __trace_id=20240726211402854272999889831347686; pos_9_end=1721999642915; ad_ids=2533482%2C3618801%2C2723440%2C2533488%7C%233%2C3%2C3%2C1; pos_6_end=1721999642965; pos_6_start=1721999855272",
        "dnt": "1",
        "host": "category.dangdang.com",
        "pragma": "no-cache",
        "referer": "https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=my_headers)
    tree = etree.HTML(resp.text)
    pages = tree.xpath(".//ul[@name='Fy']/li[last()-2]//text()")
    pages = int("".join(pages))
    for i in range(1, pages):
        if i == 1:
            url = "https://category.dangdang.com/cp01.01.02.00.00.00.html"
        else:
            url = f"https://category.dangdang.com/pg{i}-cp01.01.02.00.00.00.html"
        get_one_page_data(url)
        print(f"=============第{i}页的数据抓取完毕")

if __name__ == '__main__':
    main()
    # https://www.dushu.com/book/1188_3.html 可以做做练习. 很简答
