from core.low.stark_reqs import get_stark_data
from core.low.lists import webshare_proxy_format
import random


with open('proxy.txt') as file:
    proxy = file.readlines()
    proxy = webshare_proxy_format(proxy)


def parse_all_wallet_data(wallet:str):
    proxy_ch = 0
    while True:
        stark_data = get_stark_data(wallet,random.choice(proxy))
        if stark_data == False:
            # print(proxy_ch,'error')
            proxy_ch = proxy_ch + 1
            if proxy_ch >= len(proxy) - 1:
                proxy_ch = 0
            continue
        break
    return stark_data
