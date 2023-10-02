from core.const import chains_list
from core.low.lists import calculate_coins_balances, calculate_project_balances, calculate_total_chains
from core.low.lists import list_to_excel

def build(all_chains_data,wallet):
    formed_for_excel_data = []
    formed_for_excel_data.append(wallet)
    formed_for_excel_list = []
    formed_for_excel_list.append(None)
    chains_coins = calculate_coins_balances(all_chains_data['balance_raw_data']['data'])
    chains_projects = calculate_project_balances(all_chains_data['project_raw_data']['data'])
    chains_coins_total = calculate_total_chains(chains_coins)
    chains_projects_total = calculate_total_chains(chains_projects)
    pall = 0
    ball = 0
    for i in chains_projects_total:
        pall = chains_projects_total[i] + pall
    for i in chains_coins_total:
        ball = chains_coins_total[i] + ball

    formed_for_excel_data.append(round(pall+ball,2))
    formed_for_excel_list.append(None)

    formed_for_excel_data.append(round(pall,2))
    formed_for_excel_list.append(None)

    for i in chains_list:
        formed_for_excel_data.append(chains_coins_total[i])
        formed_for_excel_list.append(list_to_excel(chains_coins[i]))

        formed_for_excel_data.append(chains_projects_total[i])
        formed_for_excel_list.append(list_to_excel(chains_projects[i]))

        formed_for_excel_data.append(f"{chains_projects[i][0]['symbol']} {chains_projects[i][0]['usd_amount']}")
        formed_for_excel_list.append(None)

    return formed_for_excel_data, formed_for_excel_list

