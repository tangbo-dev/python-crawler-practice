
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue   # 此队列是用的网络地址.
import requests
from lxml import etree
# from queue import Queue  # 内存层面的. 进程通信. 它是不行的.....

# # 多线程的思路
# def get_img_src(url):
#     # url = "https://www.doutupk.com/article/list/?page=2"
#
#     # 请求页面源代码的
#     session = requests.session()
#     session.headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "accept-encoding": "gzip, deflate, br, zstd",
#         "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#         "cache-control": "no-cache",
#         "connection": "keep-alive",
#         "cookie": "Hm_lvt_2fc12699c699441729d4b335ce117f40=1722854195; HMACCOUNT=0BFAD8D83E97B549; _agep=1722854196; _agfp=414e8104b6865c31d12fcb23577d6d2f; _agtk=d54fe6a5787ad6ad778e047482151b24; XSRF-TOKEN=eyJpdiI6Ik5Qd1hBdElldEtnajdodWxxQ0Nlb0E9PSIsInZhbHVlIjoiYjA1a1wvSTg1em1HSzF2U0N6WEFQWEZVNW44M3ozYVZqV01rZksyOW4zYzlFNXM3cjBDbW5zZjB3Sk9PeGZuWkMiLCJtYWMiOiIyNjM4ZGE4ODc1MmVhZTRiMGM2MDI1ZDg5NDQwZDNiZjU3ZmFhMzNjNjMyZjc5MmQ0MWZiODNlYTc0MDAwMjQ1In0%3D; doutula_session=eyJpdiI6IjNlV05YWVhCSTRyM0xZZWdzTVwvWUJnPT0iLCJ2YWx1ZSI6Imt5MU5PQWdNS3YyWWJMekozMFFxQThmWHJuZGVyOWdTQkk1bzBFU1RFdnIxU2hxUlNBTlNMQVhLNXVPMHpOVGEiLCJtYWMiOiJmODAzMjBhOTM2ZTEyY2NjODAyN2RhOTY1ZjNkYjNiOTZmZjJjMjBiMDI5ODhmY2E0YmQ3Nzk5Njc2NDk4MTAxIn0%3D; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1722865156",
#         "dnt": "1",
#         "host": "www.doutupk.com",
#         "pragma": "no-cache",
#         "referer": "https://www.doutupk.com/article/list/",
#         "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "document",
#         "sec-fetch-mode": "navigate",
#         "sec-fetch-site": "same-origin",
#         "sec-fetch-user": "?1",
#         "upgrade-insecure-requests": "1",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
#     }
#
#     resp = session.get(url)
#     tree = etree.HTML(resp.text)
#
#     # n种...写法. 怎么写都OK...
#     a_list = tree.xpath("//div[@id='home']/div[1]/div[2]/a")
#     for a in a_list:
#         srcs = a.xpath(".//img/@data-original")
#         for src in srcs:
#             print(src)  # 目标是这个...
#             download_img(src)
#
#
# def download_img(src):
#     # 下载图片的.
#     session_2 = requests.session()
#     session_2.headers = {
#         "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
#         "accept-encoding": "gzip, deflate, br, zstd",
#         "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#         "cache-control": "no-cache",
#         "connection": "keep-alive",
#         "dnt": "1",
#         "host": "img.doutupk.com",
#         "pragma": "no-cache",
#         "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "image",
#         "sec-fetch-mode": "no-cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
#     }
#     file_name = src.split("/")[-1]
#     img_resp = session_2.get(src)
#     with open(file_name, mode="wb") as f:
#         f.write(img_resp.content)
#
#
# def main():
#     with ThreadPoolExecutor(10) as t:
#         # 线程池放在这里. 相当于一个url, 一个线程...
#         for i in range(2, 20):  # 2-19页
#             t.submit(get_img_src, f"https://www.doutupk.com/article/list/?page={i}")
#
#
# if __name__ == '__main__':
#     main()


# 生产者消费者模型逻辑:
def get_img_src(url, q):
    # url = "https://www.doutupk.com/article/list/?page=2"

    # 请求页面源代码的
    session = requests.session()
    session.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "Hm_lvt_2fc12699c699441729d4b335ce117f40=1722854195; HMACCOUNT=0BFAD8D83E97B549; _agep=1722854196; _agfp=414e8104b6865c31d12fcb23577d6d2f; _agtk=d54fe6a5787ad6ad778e047482151b24; XSRF-TOKEN=eyJpdiI6Ik5Qd1hBdElldEtnajdodWxxQ0Nlb0E9PSIsInZhbHVlIjoiYjA1a1wvSTg1em1HSzF2U0N6WEFQWEZVNW44M3ozYVZqV01rZksyOW4zYzlFNXM3cjBDbW5zZjB3Sk9PeGZuWkMiLCJtYWMiOiIyNjM4ZGE4ODc1MmVhZTRiMGM2MDI1ZDg5NDQwZDNiZjU3ZmFhMzNjNjMyZjc5MmQ0MWZiODNlYTc0MDAwMjQ1In0%3D; doutula_session=eyJpdiI6IjNlV05YWVhCSTRyM0xZZWdzTVwvWUJnPT0iLCJ2YWx1ZSI6Imt5MU5PQWdNS3YyWWJMekozMFFxQThmWHJuZGVyOWdTQkk1bzBFU1RFdnIxU2hxUlNBTlNMQVhLNXVPMHpOVGEiLCJtYWMiOiJmODAzMjBhOTM2ZTEyY2NjODAyN2RhOTY1ZjNkYjNiOTZmZjJjMjBiMDI5ODhmY2E0YmQ3Nzk5Njc2NDk4MTAxIn0%3D; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1722865156",
        "dnt": "1",
        "host": "www.doutupk.com",
        "pragma": "no-cache",
        "referer": "https://www.doutupk.com/article/list/",
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

    resp = session.get(url)
    tree = etree.HTML(resp.text)


    a_list = tree.xpath("//div[@id='home']/div[1]/div[2]/a")
    for a in a_list:
        srcs = a.xpath(".//img/@data-original")
        for src in srcs:
            print(src)  # 目标是这个...
            # download_img(src)  # 需要交出去. 而不是自己去下载...
            # 把src传递给队列 , '{"num": 1, "src": "xxxxxxxxx"}'  传递json就OK了呀..
            q.put(src)  # 像队列中传递一个内容


def get_img_process(q):
    with ThreadPoolExecutor(3) as t:
        # 线程池放在这里. 相当于一个url, 一个线程...
        for i in range(2, 5):  # 2-5页
            t.submit(get_img_src, f"https://www.doutupk.com/article/list/?page={i}", q)
    # 当整个任务结束的时候. 传递一个结束的信号...
    q.put("进程有误")
    print("此处, 所有图片下载地址获取完毕. 生产者, 结束....")


def download_img(src):
    # 下载图片的.
    session_2 = requests.session()
    session_2.headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "dnt": "1",
        "host": "img.doutupk.com",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    file_name = src.split("/")[-1]
    img_resp = session_2.get(src)
    with open(file_name, mode="wb") as f:
        f.write(img_resp.content)


def download_process(q):  # 消费者这边需要得到生产者那边获取到的图片下载地址
    with ThreadPoolExecutor(10) as t:
        while 1:
            # 从队列中提取到src
            src = q.get()
            if src == "进程有误":  # 接收到这条消息代表任务结束
                break
            t.submit(download_img, src)
    print("此处, 所有文件下载完毕. 消费者, 结束....")


def main():
    # 创建队列
    q = Queue()

    # 负责生产...获取图片下载地址
    p1 = Process(target=get_img_process, args=(q, ))   # args 表示给进程函数提供参数,必须是(元组)
    # 负责消费...完成图片的下载
    p2 = Process(target=download_process, args=(q, ))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

