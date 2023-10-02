
from requests import get

def get_stark_data(wallet:str,proxy=None):
    project_balances = "https://stack.starkendefi.xyz/starken/alltimeuserdata/"+wallet.lower()
    try:
        data = get(project_balances,proxies={'https':proxy},timeout=120).json()
        # print(data['score'])
        if 'score' in data.keys():
            return data
        else:
            print('parsing error')
            return False
    except:
        print('parsing error')
        return False