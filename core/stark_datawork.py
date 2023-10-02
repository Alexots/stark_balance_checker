from core.low.stark_list import calculate_project_balances, calculate_coins_balances, calculate_balance_no_nft
from core.low.stark_list import list_to_excel
import time
import random
def stark_build(data,wallet):
    time.sleep(random.randint(10,60))
    formed_for_excel_data = []
    formed_for_excel_data.append(wallet)
    formed_for_excel_list = []
    formed_for_excel_list.append(None)

    coins = calculate_coins_balances(data['data']['data_1D'][0])
    projects = calculate_project_balances(data['data']['data_1D'][0])
    balance_all = calculate_balance_no_nft(data['data']['data_1D'][0])
    balance_all_coins = 0
    balance_all_projects = 0

    for i in projects:
        balance_all_projects = balance_all_projects + projects[i]
    for i in coins:
        balance_all_coins = balance_all_coins + coins[i]

    formed_for_excel_data.append(balance_all)
    formed_for_excel_list.append(None)

    formed_for_excel_data.append(balance_all_projects)
    formed_for_excel_list.append(list_to_excel(projects))

    kk = list(projects.keys())
    kk = kk[0]
    formed_for_excel_data.append(f"{kk} {projects[kk]}")
    formed_for_excel_list.append(None)

    formed_for_excel_data.append(balance_all_coins)
    formed_for_excel_list.append(list_to_excel(coins))

    kk = list(coins.keys())
    kk = kk[0]
    formed_for_excel_data.append(f"{kk} {coins[kk]}")
    formed_for_excel_list.append(None)

    return formed_for_excel_data, formed_for_excel_list
