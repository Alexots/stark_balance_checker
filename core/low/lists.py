from core.const import chains_list

def webshare_proxy_format(file):
    result = []
    proxy = [i.replace('\n','') for i in file]
    for i in proxy:
        ind = 0
        for k in range(2):
            position = i.find(':',ind)
            ind = position + 1
        stroka = f"http://{i[position+1:]}@{i[:position]}"
        result.append(stroka)
    return result

def calculate_coins_balances(data):
    result = {i:[] for i in chains_list}
    sorted_result = {i:[] for i in chains_list}
    for i in data:
        coin_chain = i['chain']
        float_amount = i['amount']
        usd_amount = float_amount * i['price']
        symbol = i['symbol']
        result[coin_chain].append({'symbol':symbol,'usd_amount':round(usd_amount,2)})
    for chain in result:
        balance_to_symbol = {str(i['usd_amount']):i['symbol'] for i in result[chain]}
        balance_list = [float(i) for i in balance_to_symbol]
        balance_list.sort(reverse=True)
        sorted_result[chain] = [{'symbol':balance_to_symbol[str(i)],'usd_amount':float(i)} for i in balance_list]
    for chain in sorted_result:
        if bool(sorted_result[chain]) == False:
            sorted_result[chain].append({"symbol":"None",'usd_amount':0})

    return sorted_result

def calculate_project_balances(data):
    result = {i:[] for i in chains_list}
    sorted_result = {i:[] for i in chains_list}
    for i in data:
        project_chain = i['chain']
        project_name = i['name']
        project_balance = 0
        for asset in i['portfolio_item_list'][0]['asset_token_list']:
            project_balance = project_balance + asset['amount'] * asset['price']
        result[project_chain].append({'symbol':project_name,'usd_amount':round(project_balance,2)})
    for chain in result:
        balance_to_project = {str(i['usd_amount']):i['symbol'] for i in result[chain]}
        project_list = [float(i) for i in balance_to_project]
        project_list.sort(reverse=True)
        sorted_result[chain] = [{'symbol': balance_to_project[str(i)], 'usd_amount': float(i)} for i in project_list]
    for chain in sorted_result:
        if bool(sorted_result[chain]) == False:
            sorted_result[chain].append({"symbol":"None",'usd_amount':0})
    return sorted_result

def calculate_total_chains(calculate_balances_data):
    result = {i: 0 for i in chains_list}
    for chain in calculate_balances_data:
        chain_balance = 0
        for balance in calculate_balances_data[chain]:
            chain_balance = chain_balance + balance['usd_amount']
        result[chain] = chain_balance
    return result

def list_to_excel(data):
    final = ""
    for i in data:
        final = final + f"{i['symbol']} {i['usd_amount']},"
    return final

