from core.low.reqs import get_balance_data, get_project_data
from core.low.lists import webshare_proxy_format
import random

with open('proxy.txt') as file:
    proxy = file.readlines()
    proxy = webshare_proxy_format(proxy)


def parse_all_wallet_data(wallet:str):
    proxy_ch = 0
    while True:
        balance_data = get_balance_data(wallet,random.choice(proxy))
        if balance_data == False:
            # print(proxy_ch,'error')
            proxy_ch = proxy_ch + 1
            if proxy_ch >= len(proxy) - 1:
                proxy_ch = 0
            continue
        break
    proxy_ch = 0
    while True:
        project_data = get_project_data(wallet,random.choice(proxy))
        if project_data == False:
            # print(proxy_ch, 'error')
            proxy_ch = proxy_ch + 1
            if proxy_ch >= len(proxy) - 1:
                proxy_ch = 0
            continue
        break
    return {'project_raw_data':project_data,"balance_raw_data":balance_data}
