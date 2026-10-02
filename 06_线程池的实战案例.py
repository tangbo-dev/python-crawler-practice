""""
目标网站: http://www.boxofficecn.com/boxofficecn
目标数据:
    电影票房的数据(大陆票房)
"""

import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor

# # 单线程的逻辑:
#
# session = requests.session()
#
# session.headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "connection": "keep-alive",
#     "cookie": "Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1721017730,1721633285,1721992258,1722860399; HMACCOUNT=0BFAD8D83E97B549; __51cke__=; __tins__4287866=%7B%22sid%22%3A%201722860398620%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201722862292150%7D; __51laig__=4; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1722860492",
#     "dnt": "1",
#     "host": "www.boxofficecn.com",
#     "pragma": "no-cache",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
#
# def donwload_movie_data(year):
#     f = open(f"{year}_movie.csv", mode="w", encoding="utf-8")
#     url = f"http://www.boxofficecn.com/boxoffice{year}"
#     resp = session.get(url)
#     tree = etree.HTML(resp.text)
#     trs = tree.xpath("//table/tbody/tr")[1:]
#     for tr in trs:
#         xv = "".join(tr.xpath("./td[1]//text()")).strip()
#         nian = "".join(tr.xpath("./td[2]//text()")).strip()
#         name = "".join(tr.xpath("./td[3]//text()")).strip()
#         money = "".join(tr.xpath("./td[4]/text()")).strip()
#         f.write(f"{xv},{nian},{name},{money}\n")
#     f.close()
#
#
# def main():
#     for i in range(1994, 2025):
#         donwload_movie_data(i)
#         print(f"{i}年的数据抓取完毕")
#
#
# if __name__ == '__main__':
#     # 29.758466243743896
#     # 32.53658604621887
#     tm1 = time.time()
#     main()
#     tm2 = time.time()
#     print(tm2 - tm1)

def donwload_movie_data(year):
    print(f"{year}年的数据开始抓取")
    # 上线程池之后
    session = requests.session()
    session.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1721017730,1721633285,1721992258,1722860399; HMACCOUNT=0BFAD8D83E97B549; __51cke__=; __tins__4287866=%7B%22sid%22%3A%201722860398620%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201722862292150%7D; __51laig__=4; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1722860492",
        "dnt": "1",
        "host": "www.boxofficecn.com",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    f = open(f"{year}_movie.csv", mode="w", encoding="utf-8")
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    resp = session.get(url)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table/tbody/tr")[1:]
    for tr in trs:
        xv = "".join(tr.xpath("./td[1]//text()")).strip()
        nian = "".join(tr.xpath("./td[2]//text()")).strip()
        name = "".join(tr.xpath("./td[3]//text()")).strip()
        money = "".join(tr.xpath("./td[4]/text()")).strip()
        f.write(f"{xv},{nian},{name},{money}\n")
    f.close()
    print(f"{year}年的数据抓取完毕")

def main():
    with ThreadPoolExecutor(20) as t:
        for i in range(1994, 2025):
            # 每一年当成一个单独的任务
            # donwload_movie_data(i)
            t.submit(donwload_movie_data, i)

if __name__ == '__main__':
    tm1 = time.time()
    main()
    tm2 = time.time()
    print(tm2 - tm1)



