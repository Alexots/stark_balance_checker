from requests import get

def get_balance_data(wallet:str,proxy=None):
    project_balances = "https://api.debank.com/token/cache_balance_list?user_addr="+wallet.lower()
    try:
        data = get(project_balances,proxies={'https':proxy},timeout=10).json()
        if 'data' in data.keys():
            return data
        else:
            return False
    except:
        return False

def get_project_data(wallet:str,proxy=None):
    project_balances = "https://api.debank.com/portfolio/project_list?user_addr="+wallet.lower()
    try:
        data = get(project_balances,proxies={'https':proxy},timeout=10).json()
        if 'data' in data.keys():
            return data
        else:
            return False
    except:
        return False


