""""

网站:  https://xueqiu.com/
目标: 搞定滚动刷新

滚动刷新:
77777 9999
每一次请求. 都带着上一次请求的最后一条数据的id.
服务器
id, 内容
1
2
3
4
5
6
cookie
session的关系...
"""

import requests


last_id = ""
page = 1
has_next = True

while has_next:
    url = "https://xueqiu.com/statuses/hot/listV3.json"
    my_params = {
        "page": page,
        "last_id": last_id
    }

    my_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "cookiesu=531708310749485; device_id=88e85bb00e27dc3a7c3718e8828c68df; smidV2=20240722152632ece25be583087a4d08bd904aa9793aa5003fed877ca7e9b30; xq_a_token=aeb5755652c41b7828c9412ee90b26e08840b0c8; xqat=aeb5755652c41b7828c9412ee90b26e08840b0c8; xq_r_token=9ee9347bb54fea0445403de921297a01af9f4646; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyNDAyODc2OCwiY3RtIjoxNzIxOTkyMzc2Njg4LCJjaWQiOiJkOWQwbjRBWnVwIn0.K_pQDhKESg6RsarH1p8IkDXbFV_DkQpnqLSbdonDoW3I2jJkMUeUprfRGBVRrtATMo5PpMk0ubkdI_798eNdvMumLGZDAsJYlhOiSXIRnFlv12wkBoPkiFnYmwpsYf8fU439VjAzpNuRJoETaKsC5GV9nMV93rEdzDwcFQO30_zkyhomE9DPJJoCmW_ji25Gb9odD0e0CuxKxXiTLBewS4ujL9yy6k0hsCAt_Zbm5lfuzSkIk8ASPcDk1Uth6OpTqkgwFyUGiFovPx3K9BuSE9tJe3A6zx4252G88GpcORIWzT4eL1dl0LtFG5nm0eZxv7p6r1W2IwIK-psOaHiYfg; u=531708310749485; Hm_lvt_1db88642e346389874251b5a1eded6e3=1721633193,1721992424; HMACCOUNT=40D17769013D04CF; acw_tc=276077a117220054210816930e81e2a1005286d0713af5249318b538520f4c; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=FcykarU5H6xpIGrSsAIF7ybORS300Sj/rfVk+wrV18lwsY+wQpae9bpOSC7YHzmxxef+2KMzc5DuUBVgPDfj8A%3D%3D; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1722006002",
        "dnt": "1",
        "elastic-apm-traceparent": "00-387e3e840f172132164f7473d89f1311-4bbbb4eaa3576b1f-01",
        "host": "xueqiu.com",
        "pragma": "no-cache",
        "referer": "https://xueqiu.com/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, params=my_params, headers=my_headers)
    dic = resp.json()
    has_next = dic['has_next_page']
    data_list = dic['list']

    for data in data_list:
        last_id = data['id']
        # 此处应该是数据的保存
        print(last_id, data['title'][:10])
    print(f"===================第{page}页数据抓取完毕")
    page = page + 1
