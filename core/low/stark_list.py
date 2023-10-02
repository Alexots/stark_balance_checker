

# data = data['data']['data_1D'][0]
def calculate_coins_balances(data):
    result = {}
    for i in data.keys():
        if i.find("balance_usd_erc20_") != -1:
            result[i[len('balance_usd_erc20_'):]] = round(data[i],2)
    if bool(result) == False:
        result['None'] = 0
    sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    sorted_result = {i[0]: i[1] for i in sorted_result}
    return sorted_result

# data = data['data']['data_1D'][0]
def calculate_project_balances(data):
    result = {}
    for i in data.keys():
        if i.find("cumulated_cost_USD_lp_") != -1:
            result[i[len('cumulated_cost_USD_lp_'):]] = round(data[i],2)
    if bool(result) == False:
        result['None'] = 0
    sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    sorted_result = {i[0]:i[1] for i in sorted_result}
    return sorted_result

# data = data['data']['data_1D'][0]
def calculate_balance_no_nft(data):
    cum_cost = 0
    nft_cost = 0
    if 'cumulated_cost_USD' in data.keys():
        cum_cost = data['cumulated_cost_USD']
    for i in data.keys():
        if i.find('cumulated_cost_USD_nft_') != -1:
            nft_cost = nft_cost + data[i]
    result = cum_cost - nft_cost
    return round(result,2)


def list_to_excel(data):
    final = ""
    for i in data:
        final = final + f"{i} {data[i]},"
    return final
